def getAIScript():
    aiScript = [{'x': 0, 'y': 0, 'z': 0, 't': 0},
                {'x': 0, 'y': 0, 'z': 0, 't': 0.5},
                {'x': 0, 'y': 0, 'z': 0, 't': 1},
                {'x': 0.4375615119934082, 'y': 0, 'z': 0, 't': 1.5},
                {'x': 2.3225018978118896, 'y': 0, 'z': 0, 't': 2},
                {'x': 5.867350101470947, 'y': 0, 'z': 0, 't': 2.5},
                {'x': 11.044747352600098, 'y': 0, 'z': 0, 't': 3},
                {'x': 17.50465202331543, 'y': 0, 'z': 0, 't': 3.5},
                {'x': 25.884323120117188, 'y': 0, 'z': 0, 't': 4},
                {'x': 34.74658203125, 'y': 0, 'z': 0, 't': 4.5},
                {'x': 44.069583892822266, 'y': 0, 'z': 0, 't': 5},
                {'x': 54.65943145751953, 'y': 0, 'z': 0, 't': 5.5},
                {'x': 66.122802734375, 'y': 0, 'z': 0, 't': 6},
                {'x': 78.0541000366211, 'y': 0, 'z': 0, 't': 6.5},
                {'x': 91.21952819824219, 'y': 0, 'z': 0, 't': 7},
                {'x': 105.18639373779297, 'y': 0, 'z': 0, 't': 7.5},
                {'x': 119.4697036743164, 'y': 0, 'z': 0, 't': 8},
                {'x': 135.51438903808594, 'y': 0, 'z': 0, 't': 8.5},
                {'x': 151.75099182128906, 'y': 0, 'z': 0, 't': 9},
                {'x': 167.64767456054688, 'y': 0, 'z': 0, 't': 9.5},
                {'x': 184.52224731445312, 'y': 0, 'z': 0, 't': 10},
                {'x': 201.32044982910156, 'y': 0, 'z': 0, 't': 10.5},
                {'x': 219.16952514648438, 'y': 0, 'z': 0, 't': 11},
                {'x': 238.0905303955078, 'y': 0, 'z': 0, 't': 11.5},
                {'x': 256.24053955078125, 'y': 0, 'z': 0, 't': 12},
                {'x': 274.82763671875, 'y': 0, 'z': 0, 't': 12.5},
                {'x': 294.5118713378906, 'y': 0, 'z': 0, 't': 13},
                {'x': 314.62164306640625, 'y': 0, 'z': 0, 't': 13.5},
                {'x': 335.1677551269531, 'y': 0, 'z': 0, 't': 14},
                {'x': 356.15447998046875, 'y': 0, 'z': 0, 't': 14.5},
                {'x': 376.8313903808594, 'y': 0, 'z': 0, 't': 15},
                {'x': 398.6264953613281, 'y': 0, 'z': 0, 't': 15.5},
                {'x': 420.83038330078125, 'y': 0, 'z': 0, 't': 16},
                {'x': 442.6594543457031, 'y': 0, 'z': 0, 't': 16.5},
                {'x': 465.5643310546875, 'y': 0, 'z': 0, 't': 17},
                {'x': 488.17437744140625, 'y': 0, 'z': 0, 't': 17.5},
                {'x': 510.9952392578125, 'y': 0, 'z': 0, 't': 18},
                {'x': 535.7783203125, 'y': 0, 'z': 0, 't': 18.5},
                {'x': 560.1197509765625, 'y': 0, 'z': 0, 't': 19},
                {'x': 583.9558715820312, 'y': 0, 'z': 0, 't': 19.5},
                {'x': 609.3411865234375, 'y': 0, 'z': 0, 't': 20},
                {'x': 633.3779907226562, 'y': 0, 'z': 0, 't': 20.5},
                {'x': 658.359375, 'y': 0, 'z': 0, 't': 21},
                {'x': 682.7456665039062, 'y': 0, 'z': 0, 't': 21.5},
                {'x': 708.2183837890625, 'y': 0, 'z': 0, 't': 22},
                {'x': 733.8132934570312, 'y': 0, 'z': 0, 't': 22.5},
                {'x': 758.7869873046875, 'y': 0, 'z': 0, 't': 23},
                {'x': 784.0537719726562, 'y': 0, 'z': 0, 't': 23.5},
                {'x': 810.2264404296875, 'y': 0, 'z': 0, 't': 24},
                {'x': 836.6637573242188, 'y': 0, 'z': 0, 't': 24.5},
                {'x': 862.4595336914062, 'y': 0, 'z': 0, 't': 25},
                {'x': 889.2712402343750, 'y': 0, 'z': 0, 't': 25.5},
                {'x': 914.50274658203120, 'y': 0, 'z': 0, 't': 26},
                {'x': 942.61517333984380, 'y': 0, 'z': 0, 't': 26.5},
                {'x': 969.92449951171880, 'y': 0, 'z': 0, 't': 27},
                {'x': 997.5036621093750, 'y': 0, 'z': 0, 't': 28},
                {'x': 1024.32519531250, 'y': 0, 'z': 0, 't': 28.5},
                {'x': 1052.2062988281250, 'y': 0, 'z': 0, 't': 29},
                {'x': 1079.319824218750, 'y': 0, 'z': 0, 't': 29.5},
                {'x': 1107.51916503906250, 'y': 0, 'z': 0, 't': 30}]

    return aiScript