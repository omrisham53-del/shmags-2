# The £116 Million Illusion

*Nottingham Forest just received the biggest transfer fee in British history. Here's why it changes almost nothing.*

**Through the Gap | July 2026**

---

On July 2nd, Manchester City paid £116 million for Elliot Anderson. A British record. More than Declan Rice. More than Jack Grealish. The third biggest fee in Premier League history, handed to Nottingham Forest for a 23-year-old midfielder who led the league in touches, duels won and possessions recovered last season.

For Forest fans, it looked like the moment everything changes. That kind of money buys a squad rebuild. That kind of money closes gaps.

It doesn't. And the reason it doesn't is the most important story in English football right now.

**[CHART 1: Where the £116m actually goes. Stacked horizontal bar: PSR compliance hole (~£50m+), reinvestment on replacements (~£60-70m), net competitive gain (the sliver that remains). One bar, three colours, the point made before a word of explanation.]**

## Selling wasn't a choice

To understand why, you need to know what state Forest's books were in before City came calling.

The Premier League's Profitability and Sustainability Rules (PSR) allowed clubs to lose £105 million over a rolling three-year window. Forest know exactly what happens when you cross that line: in March 2024 they were docked four points for exceeding their threshold by £34.5 million. Last season they posted a £79 million loss, taking their three-year losses to £134 million before adjustments.

Read those numbers again, then look at the fee. £116 million sounds like a war chest. Against a £134 million hole, it's a lifeline.

This is why Forest's reinvestment plans total roughly £60-70 million, not £116 million: a couple of midfielders, a goalkeeper, a centre-back. The rest of Anderson's fee doesn't buy players. It buys compliance. Forest didn't sell their best player to get stronger. They sold him to stay legal.

**[CHART 2: Forest's PSR position by season. Bars for annual losses across the three-year window, the £105m limit as a hard line, the Anderson fee as an annotation arrow showing what it plugs.]**

## Three leagues in one

Forest aren't an outlier. They're one of three kinds of club that now share a division while playing completely different financial games.

**The Giants.** Manchester City, Arsenal, Liverpool. Revenues so large that the rules, old or new, never really bind. They buy the Andersons.

**The Climbers.** Brighton, Brentford. Small revenues, elite intelligence. They beat the market with data and player trading, and every summer they sell their best work to the tier above.

**The Survivors.** Forest, Everton, Leicester. Locked in a loop: spend to stay up, breach the rules, sell your best player to comply, get weaker, spend to stay up again.

The Anderson transfer is what it looks like when the top of this food chain feeds on the middle. A record fee moves from a Giant to a Survivor, and the table doesn't move at all.

**[CHART 3: All 20 Premier League clubs, revenue vs 85% spending ceiling, sorted top to bottom. Horizontal bars. Man City's ceiling alone is larger than most clubs' entire revenue.]**

## The flat tax problem

From next season, PSR is gone. Its replacement is the Squad Cost Ratio (SCR): every club may spend up to 85% of its revenue on squad costs.

The same percentage for everyone. It sounds fair. It's the same logic as a flat tax, and it fails the same way.

If two people earn £20,000 and £200,000 and both pay 20% tax, the rate is equal and the outcome is not. One keeps £16,000, the other £160,000. Nobody calls that a level playing field.

Now run it in football terms. Manchester City's revenue is around £715 million, so 85% gives them a spending ceiling of just over £600 million. Forest's revenue is around £170 million, so their ceiling is roughly £145 million. Same rule. Same percentage. A permanent gap of more than £460 million, written into the regulations.

Under PSR, a club could at least gamble: absorb losses, spend ahead of its revenue, and try to jump tiers. It was reckless, and clubs got punished for it, but the ladder existed. The SCR removes the ladder. Your spending is now chained to your revenue, and your revenue is chained to your stadium, your history and your global brand. The only clubs whose ceilings rise meaningfully each year are the ones already at the top.

**[CHART 4: The flat tax, twice. Left panel: two taxpayers at 20%. Right panel: City, Brighton and Forest at 85% SCR. Identical visual structure so the analogy lands without explanation.]**

## The vote

None of this was an accident. It was a decision, and we know just enough about it to see whose decision it was.

On November 21st, 2025, the twenty Premier League clubs voted on the new rules at a private shareholders' meeting. The SCR passed 14-6, the exact two-thirds minimum. The six clubs that voted no: Bournemouth, Brentford, Brighton, Crystal Palace, Fulham and Leeds. Every single one a small-revenue club. The clubs that had done the maths on what 85% of not-very-much actually buys.

The same meeting considered a rule that would have genuinely compressed the gap: Top-to-Bottom Anchoring, a hard cap limiting every club's squad spend to five times what the bottom club earns in central payments. With the bottom club receiving around £109 million, the cap would have sat near £545 million, and in practice constrained only the two or three biggest spenders in England.

It was voted down 12-7, with one abstention. Twelve clubs looked at the one mechanism on the table that would have bound the Giants, and killed it. The players' union had threatened legal action, calling it a salary cap by another name, which gave everyone useful cover. But the arithmetic of the room is what decided it.

And here is the detail that should bother you most: you can't look any of this up. Premier League shareholder votes are not published. The 14-6 and 12-7 figures come from briefings and leaks. The rules governing the richest football league on earth were written in a private room, by the clubs they regulate, with no public record of who raised a hand.

**[CHART 5: The vote map. Twenty club crests in two columns per vote (SCR yes/no, Anchoring yes/no), colour-coded by revenue tier. The pattern is the argument: money voted for the money rules.]**

## The gap is the point

So what did £116 million actually buy?

For Manchester City: the best ball-winning midfielder in England, replaced in their squad plans within a fortnight, at a price that barely dents a £600 million ceiling.

For Forest: a filled-in PSR hole, three or four squad players, and maybe two seasons of breathing room before the next Anderson has to be sold.

For everyone else: a preview of how this decade works. Record fees will keep flowing to the Survivors and the Climbers, and the money will keep doing what it did here: maintaining the distance rather than closing it. Under the old rules the gap was an outcome. Under the new ones it's a design feature, ratified 14 votes to 6, in a room with the doors closed.

The £116 million was real. The illusion is what it could buy.

---

**CHART SPECS (build in Python/matplotlib, consistent identity):**

1. £116m breakdown - stacked horizontal bar
2. Forest PSR window - annual losses vs £105m line + fee annotation
3. 20 clubs revenue vs 85% ceiling - sorted horizontal bars
4. Flat tax two-panel - tax example | SCR example
5. Vote map - crests/club names colour-coded by vote and revenue tier
6. (Optional, from outline) SCR ceiling vs Anchoring ceiling per club - overlaid bars; fold into Chart 5's section if the piece feels long

**VERIFY BEFORE PUBLISH:**

- [ ] Man City exact revenue figure ("around £715m" used in draft, from 2023/24 accounts knowledge - confirm latest published accounts)
- [ ] Forest exact revenue figure (~£170m used; confirm from 2024/25 accounts)
- [ ] Forest 3-year PSR position £134m "before adjustments" - confirm what adjustments (allowable deductions) do to the headline number
- [ ] Anderson fee £116m - confirm add-ons structure (is it £116m guaranteed or with add-ons?)
- [ ] Anderson stat leads (touches, duels won, possessions recovered) - confirm season and source
- [ ] Bottom club central payment £109.2m (Ipswich 2024-25) - confirm this is the anchoring reference figure
- [ ] Vote figures: SCR 14-6, Anchoring 7-12-1 - confirm against two independent reports
- [ ] The six no-voting clubs list - single-sourced so far (theesk.org via search); find second source
- [ ] SCR 30% multi-year headroom allowance - decide whether to mention (currently omitted for simplicity; a critic could say it softens the flat-tax argument)
- [ ] PSR "gone from 2026/27" - confirm no transition period overlap
