# fever
# rr
# spo2
# crp 
# CT
# 0.3f+0.3s+0.2r+0.2c

import csv
import random


#mild
mild_fever=[]
mod_fever=[]
sev_fever=[]
for i in range(50):
    mild_fever.append(random.randint(0,2)*1.25)
    mod_fever.append(random.randint(3,5)*1.25)
    sev_fever.append(random.randint(5,8)*1.25)

# rr 
mild_rr=[]
mod_rr=[]
sev_rr=[]

for i in range(50):
    mild_rr.append((random.randint(16,20)-15)/1.5)
    mod_rr.append((random.randint(20,24)-15)/1.5)
    sev_rr.append((random.randint(24,30)-15)/1.5)


## spo2
mild_sp=[]
mod_sp=[]
sev_sp=[]

# todo: mapping
for i in range(50):
    mild_sp.append(10-(random.randint(93, 98)-70)/2.8)
    mod_sp.append(10-(random.randint(85, 93)-70)/2.8)
    sev_sp.append(10-(random.randint(70, 85)-70)/2.8)



#crp
mild_crp=[]
mod_crp=[]
sev_crp=[]

for i in range(50):
    mild_crp.append((random.randint(10, 40)-10)/14.0)
    mod_crp.append((random.randint(40, 100)-10)/14.0)
    sev_crp.append((random.randint(100, 150)-10)/14.0)






mild_ct=[]
mod_ct=[]
sev_ct=[]

# todo: mapping
for i in range(50):
    mild_ct.append(random.randint(1, 8)/3)
    mod_ct.append(random.randint(9, 18)/3)
    sev_ct.append(random.randint(19, 30)/3)




fever_final=mild_fever
fever_final.extend(mod_fever)
fever_final.extend(sev_fever)



rr_final=mild_rr
rr_final.extend(mod_rr)
rr_final.extend(sev_rr)

sp_final=mild_sp
sp_final.extend(mod_sp)
sp_final.extend(sev_sp)



crp_final=mild_crp
crp_final.extend(mod_crp)
crp_final.extend(sev_crp)


ct_final=mild_ct
ct_final.extend(mod_ct)
ct_final.extend(sev_ct)


print(len(crp_final), len(sp_final), len(fever_final), len(rr_final), len(ct_final))

data=[fever_final, rr_final, sp_final, crp_final, fever_final]

  
file = open('final_test.csv', 'a+', newline ='')
  
write = csv.writer(file)
# # writing the data into the file
# with file:    
#     write.writerow(data)

for w in range(150):
    write.writerow([fever_final[w], rr_final[w], sp_final[w], crp_final[w], ct_final[w]])
file.close()




