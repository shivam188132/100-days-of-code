from prettytable import PrettyTable
table= PrettyTable()
table.add_column("Pokeymon Name",["pikachu","squirtle","charmander"] )
table.add_column("Type", ["electric","water","fire"])
table.align="l"
print(table)