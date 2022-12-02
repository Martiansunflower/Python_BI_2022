#!/usr/bin/env python
# coding: utf-8

# In[210]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[129]:


#first task
#functions for reading gff and bed6 files
def read_gff(path_to_gff_file):
    df_gff = pd.read_csv(path_to_gff_file,
                 sep='\t', 
                 header=0,
                 names=['chromosome', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'])
    return df_gff

df_gff = read_gff('/home/sweetlana/BioInf2022/Python/homework/HW5_Visualisation/rrna_annotation.gff')


# In[130]:


def read_bed6(path_to_bed_file):
    df_bed6 = pd.read_csv(path_to_bed_file, 
                      sep='\t',
                      names=['chromosome', 'start', 'end', 'name', 'score', 'strand'])
    return df_bed6

df_bed6 = read_bed6('/home/sweetlana/BioInf2022/Python/homework/HW5_Visualisation/alignment.bed')


# In[131]:


#rename column 'attributes' to shorter one
df_gff['attributes'] = df_gff['attributes'].apply(lambda x: x.split('Name=')[1].split('_')[0])
df_gff


# In[417]:


#make a table of attributes grouped by chromosome and create barplot
two_col = df_gff[['chromosome','attributes']]
table_gff = two_col.groupby('chromosome').value_counts().unstack()
table_gff.plot.bar()


# In[196]:


#intersect two files and obtain information about contigs
intersect = pd.merge(df_gff,df_bed6, on="chromosome", how="outer")
intersect[(intersect['start_x'] >= intersect['start_y']) & (intersect['end_x'] <= intersect['end_y'])]


# In[200]:


#second task
diff_data = pd.read_table('/home/sweetlana/BioInf2022/Python/homework/HW5_Visualisation/diffexpr_data.tsv.gz')


# In[416]:


fig, ax = plt.subplots(figsize=(11,6))

#put 4 segments on graph
sign_down_blue = diff_data[(diff_data['logFC'] < 0) & (diff_data['log_pval'] > 0.05)]
plt.scatter(sign_down_blue['logFC'], sign_down_blue['log_pval'], s=6,
            color='steelblue', label='Significantly downregulated')

sign_up_orange = diff_data[(diff_data['logFC'] >= 0) & (diff_data['log_pval'] > 0.05)]
plt.scatter(sign_up_orange['logFC'], sign_up_orange['log_pval'], s=6,
            color='darkorange', label='Significantly upregulated')

nonsign_down_green = diff_data[(diff_data['logFC'] < 0) & (diff_data['log_pval'] <= 0.05)]
plt.scatter(nonsign_down_green['logFC'], nonsign_down_green['log_pval'], s=6,
            color='green', label='Non-significantly downregulated')

nonsign_up_red = diff_data[(diff_data['logFC'] >= 0) & (diff_data['log_pval'] <= 0.05)]
plt.scatter(nonsign_up_red['logFC'], nonsign_up_red['log_pval'], s=6,
            color='red', label='Non-significantly upregulated')

#set labels,title and legend  
ax.set_xlabel(r'$\bf{log_2(fold \ change)}$',fontsize=12)
#here italic and bold did not work together:(
ax.set_ylabel(r'$\bf{-log_{10}(p \ value \ corrected)}$', fontsize=12) 
ax.set_title('Volcano plot', size=20, style='oblique', fontweight='bold')
ax.legend()

#separate the segments with a dotted line
plt.axvline(x = 0, linestyle='--', color='gray', linewidth=1.5)
plt.axhline(y= -np.log10(0.05), linestyle='--', color='gray', linewidth=1.5)
plt.text(7, 3, 'p value=0.05', weight='bold',  color='gray', fontsize=12)

#add minor ticks on axes
ax.minorticks_on()

#annotate genes
plt.annotate('UMOD', xy=(-10.6, 54), xytext=(-11.5, 62),fontweight='bold',
             arrowprops=dict(facecolor='red', width=3, headwidth=6, headlength=3))
plt.annotate('MUC7', xy=(-9.2, 4), xytext=(-9.8, 13), fontweight='bold', 
             arrowprops=dict(facecolor='red', width=3, headwidth=6, headlength=3))
plt.annotate('ZIC5', xy=(4.4, 6), xytext=(4, 14), fontweight='bold',
             arrowprops=dict(facecolor='red', width=3, headwidth=6, headlength=3))
plt.annotate('ZIC2', xy=(4.6, 5), xytext=(5, 12), fontweight='bold',
             arrowprops=dict(facecolor='red', width=3, headwidth=6, headlength=3))

