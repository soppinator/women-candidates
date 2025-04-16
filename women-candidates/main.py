import csv
candidates = []

with open('women_candidates_2020.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    candidates.append(row)

# how many ran in primaries for us rep
primaryRep = 0
for c in candidates:
  if c['Office'] == 'U.S. Rep.':
      primaryRep = primaryRep +1
print("2: US Rep:")
print(primaryRep)

# how many total
candidateCount = 0
for c in candidates:
    candidateCount = candidateCount +1
print("3: A: candidates:")
print(candidateCount)

# how many were democrats
democrats = 0
for c in candidates:
  if c['Party'] == 'D':
      democrats = democrats +1
print("B: democrats:")
print(democrats)

# how many were republicans
republicans = 0
for c in candidates:
  if c['Party'] == 'R':
      republicans = republicans +1
print("B: republicans:")
print(republicans)

# how many were other
other = 0
for c in candidates:
  if c['Party'] == 'NP':
      other = other +1
print("B: other:")
print(other)

# how many won
winners = 0
for c in candidates:
  if c['General'] == 'W':
      winners = winners +1
print("C: winners:")
print(winners)
print("C: winner percentage:")
print(candidateCount/winners)


# how many ran as democrat in senate and won
demSenWin = 0
for c in candidates:
  if c['Party'] == 'D' and c['General'] == 'W' and c['Office'] == 'U.S. Sen.':
      demSenWin = demSenWin +1
print("D: Democratic Senator Winners:")
print(demSenWin)

# how many lost
demSenLose = 0
for c in candidates:
  if c['Party'] == 'D' and c['General'] == 'L' and c['Office'] == 'U.S. Sen.':
      demSenLose = demSenLose +1
print("D: Democratic Senator Losers:")
print(demSenLose)

# what percentage of all women who started running for us senator successfully became senators
senRunW = 0
for c in candidates:
  if c['Office'] == 'U.S. Sen.' and c['General'] == 'W':
      senRunW = senRunW +1
print("E: Senator Winners:")
print(senRunW)

senRun = 0
for c in candidates:
  if c['Office'] == 'U.S. Sen.':
      senRun = senRun +1
print("E: Senators:")
print(senRun)

print("E: Percentage of Senator Winners:")
print(senRun/senRunW)

# Senator losses
senRunL = 0
for c in candidates:
  if c['Office'] == 'U.S. Sen.' and c['General'] == 'W':
      senRunL = senRunL +1



# did democrats or republicans have a better success rate
demWin = 0
for c in candidates:
  if c['Party'] == 'D' and c['General'] == 'W':
      demWin = demWin +1
print("F: Democratic Wins:")
print(demWin)

RepWin = 0
for c in candidates:
  if c['Party'] == 'R' and c['General'] == 'W':
      RepWin = RepWin +1
print("F: Republican Wins:")
print(RepWin)
print("F: democratic women are more likely to win than republican women")