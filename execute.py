import subprocess

def str_pro(s):
    s = s.split('\\n')
    del s[0]
    del s[-1]
    val = []
    for t in s:
        val.append(t.split(': '))
    
    return val
def execute(data):
    accuracy = {}
    f = open('test/result/'+data+'.txt','w')
    for i in range(1,108):
        img = 'test/data/'+data+'/images-%d.jpg'%i
        save_img = 'test/result/'+data+'/images-%d'%i
        s = str_pro(str(subprocess.check_output(["./darknet","detect","cfg/yolov3.cfg","yolov3.weights",img,save_img])))
        f.write('images-%d\n'%i)
        for t in s:
            f.write(t[0])
            f.write(' ')
            f.write(t[1])
            if t[0] in accuracy:
                accuracy[t[0]] = [accuracy[t[0]][0]+int(t[1][:-1]), accuracy[t[0]][1]+1]
            else:
                accuracy[t[0]] = [int(t[1][:-1]),1]
            f.write('\n')
        f.write('\n')
        print('images-%d complete'%i)
    
    f.write('\n')
    for key in accuracy.keys():
        f.write(str(key) + ' ' + str(float(accuracy[key][0])/accuracy[key][1]) + '% '  + str(accuracy[key][1]) + '개\n')
        
    f.close()

execute('origin')
execute('blur33')
execute('blur55')
execute('trans1')
execute('trans2')
