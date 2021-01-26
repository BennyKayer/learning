## Data Structure choice
Object Oriented Programming because both Backpack and Item are something psychical and easy to imagine
Custom Item object with weight and value fields
## Goal Prototype
The solution's quality can be expressed as its value
## Acceptance Requirement
The combined weight of items from the solution cannot exceed backpack capacity
## Tabu Search Pseudocode
sBest ← s0
bestCandidate ← s0
tabuList ← []
tabuList.push(s0)
while (not stoppingCondition())
	sNeighborhood ← getNeighbors(bestCandidate)
	for (sCandidate in sNeighborhood)
		if ( (not tabuList.contains(sCandidate)) and (fitness(sCandidate) > fitness(bestCandidate)) )
			bestCandidate ← sCandidate
		end
	end
	if (fitness(bestCandidate) > fitness(sBest))
		sBest ← bestCandidate
	end
	tabuList.push(bestCandidate)
	if (tabuList.size > maxTabuSize)
		tabuList.removeFirst()
	end
end
return sBest
## Hillclimb random pseudocode
    na początku generować jakieś losowe rozwiąznie
    powtarzaj zadaną liczbę razy
        generować losowe rozwiązanie z bliskiego otoczenia bieżącego rozwiązania
        sprawdzać czy jest to lepsze od bieżącego rozwiązania
        jeśli tak, to aktualizować bieżące rozwiązanie
        jeśli nie uda się poprawić przez dłuższy czas, to algorytm powinien się zakończyć
## Hillclimb full pseudocode
    na początku generować jakieś losowe rozwiąznie
    powtarzaj zadaną liczbę razy
        pobierać listę rozwiązań z otoczenia bieżącego rozwiązania
        dla każdego z tych rozwiązań sprawdzać czy jest lepsze od bieżącego rozwiązania
            jeśli tak, to aktualizować bieżące rozwiązanie
            jeśli nie uda się poprawić, to algorytm powinien się zakończyć

        