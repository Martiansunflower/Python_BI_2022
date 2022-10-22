#я очень поздно заметила примечание, что код следует разбить на маленькие функции
#а когда начала разбивать, все полетело :( 
#(извиняюсь за полотно)


def main(input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds = (0, 2**32), quality_threshold = 0, save_filtered = False):
    
    dabslash = output_file_prefix.replace("\\", "\\\\") #чтобы не кушались \t, заменяю все "\" в пути к файлу на "\\"
    outputPass_GC = dabslash + "_GC"+ "_passed.fastq"   #добавляю к названию аутпута соответствующий фильтр
    outputFail_GC = dabslash + "_GC" + "_failed.fastq"  #потому что код на данном этапе фильтрует по 1 параметру за раз 
    outputPass_Len = dabslash + "_Lengh" + "_passed.fastq"   
    outputFail_Len = dabslash + "_Lengh" + "_failed.fastq"
    outputPass_quality = dabslash + "_quality" + "_passed.fastq"   
    outputFail_quality = dabslash +"_quality" + "_failed.fastq"

    #Фильтр ридов по GC составу
    with open(input_fastq, 'r') as inp, open(outputPass_GC, 'w') as OutPass, open(outputFail_GC, 'w') as OutFail:

            #бежим по fastq-файлу
            try:
                while True:
                    label = next(inp)
                    seq = next(inp)
                    ident = next(inp)
                    asc2 = next(inp)

                    #в переменную GC сохраняю процентное соотношение GC к длине строки 
                    GC = ((seq.count('G') + seq.count('C'))/len(seq.strip())) * 100

                    #тремя уровнями if перебираю варианты: 2 числа переданы в аргумент или 1, save_filtered = False или True

                    if type(gc_bounds) == tuple:
                        if GC >= gc_bounds[0] and GC <= gc_bounds[1]:
                            OutPass.write(label + seq + ident + asc2)
                        else:
                            if save_filtered == True:
                                OutFail.write(label + seq + ident + asc2)
                        pass

                    if type(gc_bounds) == int:
                        if GC <= gc_bounds:
                            OutPass.write(label + seq + ident + asc2)
                        else:
                            if save_filtered == True:
                                OutFail.write(label + seq + ident + asc2)
                        pass
                    
            except StopIteration:
                pass
            
    #Аналогичный фильтр ридов по длине 
    with open(input_fastq, 'r') as inp, open(outputPass_Len, 'w') as OutPass, open(outputFail_Len, 'w') as OutFail:
            
            try:
                while True:
                    label = next(inp)
                    seq = next(inp)
                    ident = next(inp)
                    asc2 = next(inp)

                    #в переменную len_read кладется длина рида и сравнивается с length_bounds
                    len_read = len(seq.strip())

                    if type(length_bounds) == tuple:
                        if len_read >= length_bounds[0] and len_read <= length_bounds[1]:
                            OutPass.write(label + seq + ident + asc2)
                        else:
                            if save_filtered == True:
                                OutFail.write(label + seq + ident + asc2)
                        pass

                    if type(length_bounds) == int:
                        if len_read <= gc_bounds:
                            OutPass.write(label + seq + ident + asc2)
                        else:
                            if save_filtered == True:
                                OutFail.write(label + seq + ident + asc2)
                        pass

            except StopIteration:
                pass
            
            
    #Фильтр ридов по качеству        
    with open(input_fastq, 'r') as inp, open(outputPass_quality, 'w') as OutPass, open(outputFail_quality, 'w') as OutFail:
        
            try:
                while True:
                    label = next(inp)
                    seq = next(inp)
                    ident = next(inp)
                    asc2 = next(inp)

                    #считаю Q-Score для каждого нуклеотида в риде, затем считаю среднее значение для рида
                    q_decode = 0
                    for i in asc2:
                        q_decode += ord(i) - 33
                    mean_q = q_decode/len(asc2.strip())


                    #среднее для каждого рида (mean_q) сравнивается с пороговым значением
                    if mean_q >= quality_threshold:
                        OutPass.write(label + seq + ident + asc2)
                    else:
                        if save_filtered == True:
                            OutFail.write(label + seq + ident + asc2)
                    pass
                
            except StopIteration:
                pass