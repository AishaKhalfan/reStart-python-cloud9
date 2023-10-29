{"filter":false,"title":"calc_weight_json.py","tooltip":"/calc_weight_json.py","undoManager":{"mark":24,"position":24,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":22},"action":"insert","lines":["import jsonFileHandler"],"id":1}],[{"start":{"row":0,"column":22},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":57},"action":"insert","lines":["data = jsonFileHandler.readJsonFile('files/insulin.json')"],"id":3}],[{"start":{"row":1,"column":57},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":2,"column":0},"end":{"row":11,"column":35},"action":"insert","lines":["if data != \"\" :","    bInsulin = data['molecules']['bInsulin']","    aInsulin = data['molecules']['aInsulin']","    insulin = bInsulin + aInsulin","    molecularWeightInsulinActual = data['molecularWeightInsulinActual']","    print('bInsulin: ' + bInsulin)","    print('aInsulin: ' + aInsulin)","    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))","else:","    print(\"Error. Exiting program\")"],"id":5}],[{"start":{"row":11,"column":35},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":7}],[{"start":{"row":0,"column":22},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":12,"column":35},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":23,"column":122},"action":"insert","lines":["# Calculating the molecular weight of insulin  ","# Getting a list of the amino acid (AA) weights  ","aaWeights = data['weights']","# Count the number of each amino acids  ","aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  ","# Multiply the count by the weights  ","molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in","['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  ","print(\"The rough molecular weight of insulin: \" +","str(molecularWeightInsulin))","print(\"Percent error: \" + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))"],"id":10}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":11}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "],"id":12}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "],"id":13}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "],"id":14}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "],"id":15}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "],"id":16}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "],"id":17}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":18}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "],"id":19}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":35},"action":"remove","lines":["else:","    print(\"Error. Exiting program\")"],"id":21}],[{"start":{"row":10,"column":79},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":22}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":23}],[{"start":{"row":21,"column":126},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":23,"column":35},"action":"insert","lines":["else:","    print(\"Error. Exiting program\")"],"id":25}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "],"id":26}],[{"start":{"row":0,"column":22},"end":{"row":25,"column":0},"action":"remove","lines":["","","data = jsonFileHandler.readJsonFile('files/insulin.json')","if data != \"\" :","    bInsulin = data['molecules']['bInsulin']","    aInsulin = data['molecules']['aInsulin']","    insulin = bInsulin + aInsulin","    molecularWeightInsulinActual = data['molecularWeightInsulinActual']","    print('bInsulin: ' + bInsulin)","    print('aInsulin: ' + aInsulin)","    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))","    # Calculating the molecular weight of insulin  ","    # Getting a list of the amino acid (AA) weights  ","    aaWeights = data['weights']","    # Count the number of each amino acids  ","    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  ","    # Multiply the count by the weights  ","    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in","    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  ","    print(\"The rough molecular weight of insulin: \" +","    str(molecularWeightInsulin))","    print(\"Percent error: \" + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))","else:","    print(\"Error. Exiting program\")","    ",""],"id":27}]]},"ace":{"folds":[],"scrolltop":20,"scrollleft":0,"selection":{"start":{"row":0,"column":22},"end":{"row":25,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"072a5623071b0bc8b66f7e5e5d6e012f6db0e118","timestamp":1698607653939}