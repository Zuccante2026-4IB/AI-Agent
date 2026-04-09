from cat.mad_hatter.decorators import tool

@tool(
    examples=["calcola la tabellina", "calculate the moltiplication table"]
)
def calcola_tabellina(tool_input, cat):
    # Docstring che rappresenta il metodo in modo che l'agente lo riconosca
    """
        Calcola la tabellina del numero dato in input.
        L'input è sempre il numero di cui si vuole calcolare la tabellina.
    """
    result = ""
    for i in range(1, 11):
        result += f"{tool_input} * {i} = {tool_input * i}"

    return result # Il modello penserà a formattare il tutto