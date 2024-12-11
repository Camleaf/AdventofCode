raw = open("main.in","r").read().split("\n")
layers = [list(map(int,line.split(' '))) for line in raw]

safe = 0
for test_layer in layers:
    for j in range(len(test_layer)):
        layer = [x for x in test_layer]
        if j != len(test_layer):
            layer.pop(j)
        layer_type = "neutral"
        grading = "safe"
        grade_list = []
        for i,num in enumerate(layer):
            if i == 0: continue
            if abs(num - layer[i-1]) > 3:
                grading = "unsafe"
                break
            if num == layer[i-1]:
                grading = "unsafe"
                break
            elif num > layer[i-1]:
                if layer_type == "Dec":
                    grading = "unsafe"
                    break
                layer_type = "Inc"
            elif num < layer[i-1]:
                if layer_type == "Inc":
                    grading = "unsafe"
                    break
                layer_type = "Dec"
        if grading == "safe":
            safe+=1
            break
print(safe)
