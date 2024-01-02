def ingredients():
        return {
           "chocolate":"250g",
           "eggs":"5",
           "sugar":"125g",
           "flour":"75g",
           "butter":"175g"}

def desktop(catalog, components):
        totaal=0
        for component in components:
                totaal += catalog[component]
        return totaal
            
        
def rankings(participants):
        result = {}
        for index in range(len(participants)):
            participant = participants[index]
            ranking = index + 1
            result[participant] = ranking
        return result

def sell(stock, model):
       stock[model]-=1
       if stock[model]==0:
              del stock[model]


