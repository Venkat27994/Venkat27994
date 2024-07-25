s='''     code67        TYPE qmel-bzmng,
       code67_kg    TYPE qmel-bzmng,
       code67_disp   TYPE p LENGTH 13 DECIMALS 2,
       code67_per    TYPE p LENGTH 13 DECIMALS 2,
       code67_kg_per TYPE p LENGTH 13 DECIMALS 2,'''
for i in range(62,101):
    print('\t\tcode'+str(i)+'\t\tTYPE qmel-bzmng, code'+str(i)+'_kg\tTYPE qmel-bzmng,\n\t\tcode'+str(i)+'_disp(20)\tTYPE c,\n\t\tcode'+str(i)+'_per\tTYPE p LENGTH 13 DECIMALS 2,\n\t\tcode'+str(i)+'_kg_per TYPE p LENGTH 13 DECIMALS 2,\n\n')

