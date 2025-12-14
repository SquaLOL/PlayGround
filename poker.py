
"""
Texas Hold'em (Console) - runnable Python script

Features:
- Multiple rounds, simple blind structure (small/big), ante optional
- Betting rounds: pre-flop, post-flop, turn, river with actions: check, bet, call, raise, fold
- Simple bot opponents with basic heuristics
- Hand evaluator (best 5 of 7)
- Basic pot splitting on ties
- Save/restore stack across rounds, game ends when human or all bots bust
- Meant for educational / casual play

To run:
    python holdem_console.py

Controls (when prompted):
- For actions type: check, bet, call, raise, fold (or aliases: c, b, ca, r, f)
- When betting/raising you'll be asked an amount (integer)
"""

import itertools
import random

RANKS = "23456789TJQKA"
SUITS = "♠♥♦♣"
RANK_TO_VALUE = {r: i + 2 for i, r in enumerate(RANKS)}  # 2..14


def create_deck():
    return [r + s for r in RANKS for s in SUITS]


def card_value(card):
    return RANK_TO_VALUE[card[0]]


def pretty(cards):
    return " ".join(cards)


# === Hand evaluator (returns tuple; higher is better) ===
# Categories: 8 SF,7 Four,6 FullHouse,5 Flush,4 Straight,3 Trips,2 TwoPair,1 OnePair,0 HighCard
def evaluate_five(cards5):
    vals = sorted([card_value(c) for c in cards5], reverse=True)
    suits = [c[1] for c in cards5]
    counts = {}
    for v in vals:
        counts[v] = counts.get(v, 0) + 1
    # flush?
    suit_counts = {}
    for c in cards5:
        suit_counts[c[1]] = suit_counts.get(c[1], 0) + 1
    is_flush = any(cnt == 5 for cnt in suit_counts.values())
    # straight?
    unique_vals = sorted(set(vals))

    def straight_high(vals_list):
        vs = vals_list[:]
        if 14 in vs:
            vs = [1] + vs
        consec = 1
        best = None
        for i in range(1, len(vs)):
            if vs[i] == vs[i - 1] + 1:
                consec += 1
            elif vs[i] == vs[i - 1]:
                pass
            else:
                consec = 1
            if consec >= 5:
                best = vs[i]
        # also check whole run starting at idx0
        # simplified because in 5 cards we can just test compositions
        # fallback manual check for A-2-3-4-5
        if set([14, 2, 3, 4, 5]).issubset(set(vals_list)):
            return 5
        return best

    sh = straight_high(sorted(set(vals)))
    # counts grouping
    groups = sorted(((cnt, val) for val, cnt in counts.items()), reverse=True)
    # groups e.g. [(3,14),(1,13),(1,12)]
    if is_flush and sh:
        return (8, sh)
    # four
    for val, cnt in counts.items():
        if cnt == 4:
            kicker = max(v for v in vals if v != val)
            return (7, val, kicker)
    # full house
    trips = sorted([v for v, c in counts.items() if c == 3], reverse=True)
    pairs = sorted([v for v, c in counts.items() if c == 2], reverse=True)
    if trips and (pairs or len(trips) > 1):
        three = trips[0]
        if pairs:
            pair = pairs[0]
        else:
            pair = trips[1]
        return (6, three, pair)
    if is_flush:
        return (5,) + tuple(sorted(vals, reverse=True))
    if sh:
        return (4, sh)
    if trips:
        t = trips[0]
        kickers = sorted([v for v in vals if v != t], reverse=True)[:2]
        return (3, t) + tuple(kickers)
    if len(pairs) >= 2:
        top2 = sorted([v for v in pairs], reverse=True)[:2]
        kicker = max(v for v in vals if v not in top2)
        return (2, top2[0], top2[1], kicker)
    if len(pairs) == 1:
        p = pairs[0]
        kickers = sorted([v for v in vals if v != p], reverse=True)[:3]
        return (1, p) + tuple(kickers)
    return (0,) + tuple(sorted(vals, reverse=True)[:5])


def best_hand_from_seven(cards7):
    best = None
    best_combo = None
    for combo in itertools.combinations(cards7, 5):
        val = evaluate_five(list(combo))
        if best is None or val > best:
            best = val
            best_combo = combo
    return best, best_combo


# === Player and Game logic ===
class Player:
    def __init__(self, name, chips=200, is_human=False):
        self.name = name
        self.chips = chips
        self.hole = []
        self.folded = False
        self.allin = False
        self.current_bet = 0
        self.is_human = is_human

    def reset_for_round(self):
        self.hole = []
        self.folded = False
        self.allin = False
        self.current_bet = 0

    def __str__(self):
        flag = "You" if self.is_human else "Bot"
        status = " (ALL-IN)" if self.allin else ""
        return f"{self.name} [{flag}] chips:{self.chips}{status}"


# Simple bot decision engine (returns action + amount_if_needed)
def bot_decision(player, community_cards, to_call, min_raise, pot, stage):
    """
    stage: 'pre', 'flop', 'turn', 'river'
    Simple heuristic:
    - Evaluate hole strength roughly by high card and pair in hole
    - If to_call == 0: sometimes check or make small bet
    - If facing bet: call sometimes, fold rarely if weak
    """
    ranks = sorted([card_value(c) for c in player.hole], reverse=True)
    high = ranks[0]
    has_pair_in_hole = ranks[0] == ranks[1]
    r = random.random()
    # stronger on later streets slightly more conservative
    if to_call == 0:
        # choose to bet sometimes
        if has_pair_in_hole or high >= 12:
            if r < 0.6:
                # bet small fraction
                amt = min(player.chips, max(min_raise, int(pot * 0.2)))
                return ('bet', amt)
            else:
                return ('check', 0)
        else:
            if r < 0.15:
                return ('bet', min(player.chips, min_raise))
            return ('check', 0)
    else:
        # facing bet
        # If pair or high and not too large, call
        if has_pair_in_hole or high >= 11:
            if r < 0.8:
                return ('call', to_call)
            else:
                # occasionally raise
                if player.chips > to_call + min_raise and r > 0.95:
                    return ('raise', min(player.chips, to_call + min_raise))
                return ('call', to_call)
        else:
            # weak
            if r < 0.35:
                return ('call', to_call)
            else:
                return ('fold', 0)


# Helpers for user input
def ask(prompt, valid=None, default=None):
    val = input(prompt).strip().lower()
    if val == "" and default is not None:
        return default
    if valid:
        if val in valid:
            return val
        # map common aliases
        aliases = {'c': 'check', 'b': 'bet', 'ca': 'call', 'r': 'raise', 'f': 'fold'}
        if val in aliases:
            return aliases[val]
        print("Неверный ввод. Попробуйте ещё раз.")
        return ask(prompt, valid, default)
    return val


def ask_int(prompt, default=None, minv=0, maxv=None):
    s = input(prompt).strip()
    if s == "" and default is not None:
        return default
    try:
        v = int(s)
        if v < minv:
            print("Меньше допустимого.")
            return ask_int(prompt, default, minv, maxv)
        if maxv is not None and v > maxv:
            print("Больше допустимого.")
            return ask_int(prompt, default, minv, maxv)
        return v
    except:
        print("Введите целое число.")
        return ask_int(prompt, default, minv, maxv)


# Betting round engine
def betting_round(players, dealer_idx, starting_idx, min_raise, pot, to_call_initial=0, community=None, stage='pre'):
    """
    players: list of Player objects in seat order
    dealer_idx: index of dealer (for info)
    starting_idx: index to act first
    min_raise: minimal raise amount
    pot: current pot (int)
    Returns updated pot and index of last aggressor (for turn order)
    """
    # Reset current_bet for this round? Usually carry across; assume current_bet tracked per round
    active_players = [p for p in players if not p.folded and p.chips > 0]
    if len(active_players) <= 1:
        return pot
    # to_call: amount players need to put to call current highest bet
    current_high = max(p.current_bet for p in players)
    to_call = lambda p: max(0, current_high - p.current_bet)
    idx = starting_idx
    last_raiser = None
    # We'll loop until every active player has either called current_high or folded or is allin
    while True:
        p = players[idx]
        if not p.folded and not p.allin:
            need = to_call(p)
            if p.is_human:
                print(f"\nПозиция: {p.name} | Стеки: {p.chips} | Текущий вклад: {p.current_bet} | Для колла: {need}")
                print("Сообщаемая ставка на столе:", pretty(community) if community else "(нет)")
                if need == 0:
                    action = ask("Ваш ход (check/bet/fold) [c/b/f]: ", valid=['check', 'bet', 'fold'], default='check')
                    if action == 'check':
                        pass
                    elif action == 'bet':
                        amt = ask_int(f"Сколько поставить? (min {min_raise}, max {p.chips}): ", default=min_raise,
                                      minv=min_raise, maxv=p.chips)
                        amt = min(amt, p.chips)
                        p.chips -= amt
                        p.current_bet += amt
                        pot += amt
                        current_high = max(current_high, p.current_bet)
                        last_raiser = idx
                    elif action == 'fold':
                        p.folded = True
                else:
                    # facing bet
                    action = ask("Ваш ход (call/raise/fold) [ca/r/f]: ", valid=['call', 'raise', 'fold'],
                                 default='call')
                    if action == 'call':
                        pay = min(need, p.chips)
                        p.chips -= pay
                        p.current_bet += pay
                        pot += pay
                        if p.chips == 0:
                            p.allin = True
                    elif action == 'raise':
                        # must raise by at least min_raise on top of need
                        min_amount = need + min_raise
                        if min_amount > p.chips:
                            # cannot raise -> all-in call
                            pay = p.chips
                            p.chips -= pay
                            p.current_bet += pay
                            pot += pay
                            p.allin = True
                        else:
                            amt = ask_int(f"Сколько выставить (минимум {min_amount}, максимум {p.chips}): ",
                                          default=min_amount, minv=min_amount, maxv=p.chips)
                            pay = amt
                            p.chips -= pay
                            p.current_bet += pay
                            pot += pay
                            current_high = max(current_high, p.current_bet)
                            last_raiser = idx
                    elif action == 'fold':
                        p.folded = True
            else:
                # bot
                action, amt = bot_decision(p, community, need, min_raise, pot, stage)
                if action == 'check':
                    pass
                elif action == 'bet':
                    bet_amt = min(p.chips, max(min_raise, amt))
                    bet_amt = max(bet_amt, min_raise)
                    bet_amt = min(bet_amt, p.chips)
                    p.chips -= bet_amt
                    p.current_bet += bet_amt
                    pot += bet_amt
                    current_high = max(current_high, p.current_bet)
                    last_raiser = idx
                    print(f"{p.name} bets {bet_amt}")
                elif action == 'call':
                    pay = min(need, p.chips)
                    p.chips -= pay
                    p.current_bet += pay
                    pot += pay
                    if p.chips == 0:
                        p.allin = True
                    print(f"{p.name} calls {pay}")
                elif action == 'raise':
                    # amt is total desired, ensure legal
                    desired = amt
                    if desired < need + min_raise:
                        desired = need + min_raise
                    desired = min(desired, p.chips)
                    p.chips -= desired
                    p.current_bet += desired
                    pot += desired
                    current_high = max(current_high, p.current_bet)
                    last_raiser = idx
                    print(f"{p.name} raises to {p.current_bet}")
                elif action == 'fold':
                    p.folded = True
                    print(f"{p.name} folds")
        # advance index
        idx = (idx + 1) % len(players)
        # Check termination: all active players either folded or have current_bet == current_high or are all-in
        ongoing = False
        for q in players:
            if q.folded or q.allin:
                continue
            if q.current_bet != current_high:
                ongoing = True
                break
        if not ongoing:
            break
    # reset current_bet remains as is (pot contains amounts), but for next betting round we must zero current_bet after pot accounted for
    return pot


def settle_pot_and_showdown(players, community, pot):
    active = [p for p in players if not p.folded]
    if len(active) == 1:
        winner = active[0]
        winner.chips += pot
        print(f"\nВсе сбросили карты. Победитель {winner.name} получает банк {pot}.")
        return
    results = []
    for p in active:
        best_val, combo = best_hand_from_seven(p.hole + community)
        results.append((p, best_val, combo))
        print(f"{p.name}: {pretty(p.hole)} -> {pretty(combo)} | сила {best_val}")
    best_value = max(r[1] for r in results)
    winners = [r[0] for r in results if r[1] == best_value]
    split = pot // len(winners)
    for w in winners:
        w.chips += split
    if len(winners) == 1:
        print(f"\nПобедитель: {winners[0].name} получает {split} (банк {pot}).")
    else:
        print(f"\nНичья между: {', '.join(w.name for w in winners)} — каждый получает {split} (банк {pot}).")


def play_game(num_bots=3, starting_chips=200, small_blind=5, big_blind=10, max_rounds=100):
    # Setup players (user at position 0)
    players = [Player("You", chips=starting_chips, is_human=True)]
    for i in range(num_bots):
        players.append(Player(f"Bot{i + 1}", chips=starting_chips))
    dealer_idx = 0  # dealer button index
    round_no = 0
    while round_no < max_rounds:
        round_no += 1
        print("\n" + "=" * 40)
        print(f"Round {round_no} — Dealer: {players[dealer_idx].name}")
        # filter out busted players
        players = [p for p in players if p.chips > 0]
        if len(players) <= 1:
            print("Игра окончена — недостаточно игроков.")
            break
        # rotate dealer
        dealer_idx = dealer_idx % len(players)
        # reset per-round state
        for p in players:
            p.reset_for_round()
        # prepare deck and deal
        deck = create_deck()
        random.shuffle(deck)
        for p in players:
            p.hole = [deck.pop(), deck.pop()]
        pot = 0
        # Blinds: sb next to dealer, bb next
        sb_idx = (dealer_idx + 1) % len(players)
        bb_idx = (dealer_idx + 2) % len(players)
        # Posting blinds
        sb_amt = min(small_blind, players[sb_idx].chips)
        bb_amt = min(big_blind, players[bb_idx].chips)
        players[sb_idx].chips -= sb_amt
        players[sb_idx].current_bet = sb_amt
        players[bb_idx].chips -= bb_amt
        players[bb_idx].current_bet = bb_amt
        pot += sb_amt + bb_amt
        print(f"Small blind {players[sb_idx].name} posts {sb_amt}; Big blind {players[bb_idx].name} posts {bb_amt}")
        # Pre-flop betting: first action is player after BB
        first_idx = (bb_idx + 1) % len(players)
        min_raise = big_blind
        # Pre-flop betting
        pot = betting_round(players, dealer_idx, first_idx, min_raise, pot, community=[])
        # Move community: flop
        for p in players:
            p.current_bet = 0  # clear table bets carried into pot already

        active = [p for p in players if not p.folded and p.chips > 0]
        if len(active) == 1:
            active[0].chips += pot
            print(f"{active[0].name} единственный оставшийся — получает {pot}")
            dealer_idx = (dealer_idx + 1) % len(players)
            continue
        deck.pop()
        flop = [deck.pop(), deck.pop(), deck.pop()]
        print("\nФлоп:", pretty(flop))
        first_idx = (dealer_idx + 1) % len(players)
        pot = betting_round(players, dealer_idx, first_idx, min_raise, pot, community=flop, stage='flop')
        for p in players:
            p.current_bet = 0
        active = [p for p in players if not p.folded and (p.chips > 0 or p.allin)]
        if len(active) == 1:
            active[0].chips += pot
            print(f"{active[0].name} единственный оставшийся — получает {pot}")
            dealer_idx = (dealer_idx + 1) % len(players)
            continue
        deck.pop()
        turn = deck.pop()
        community = flop + [turn]
        print("\nТерн:", turn, " | Community:", pretty(community))
        pot = betting_round(players, dealer_idx, (dealer_idx + 1) % len(players), min_raise, pot, community=community,
                            stage='turn')
        for p in players:
            p.current_bet = 0
        active = [p for p in players if not p.folded and (p.chips > 0 or p.allin)]
        if len(active) == 1:
            active[0].chips += pot
            print(f"{active[0].name} единственный оставшийся — получает {pot}")
            dealer_idx = (dealer_idx + 1) % len(players)
            continue
        deck.pop()
        river = deck.pop()
        community = flop + [turn, river]
        print("\nРивер:", river, " | Community:", pretty(community))
        pot = betting_round(players, dealer_idx, (dealer_idx + 1) % len(players), min_raise, pot, community=community,
                            stage='river')
        for p in players:
            p.current_bet = 0
        settle_pot_and_showdown(players, community, pot)
        dealer_idx = (dealer_idx + 1) % len(players)
        print("\nСтеки после раунда:")
        for p in players:
            print(p)
        human = next((p for p in players if p.is_human), None)
        if human is None or human.chips <= 0:
            print("У вас нет фишек. Игра окончена.")
            break
        cont = ask("Играть ещё раунд? (y/n) [y]: ", valid=['y', 'n'], default='y')
        if cont != 'y':
            print("Выход из игры.")
            break
    print("Спасибо за игру!")


if __name__ == "__main__":
    try:
        nb = int(input("Сколько ботов? (1-6) [3]: ") or "3")
    except:
        nb = 3
    play_game(num_bots=nb)
