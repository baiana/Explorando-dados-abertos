
# coding: utf-8

# <h1> Exploração de dados abertos: Preços de remédios</h1>

# In[1]:



import pandas as pd

remedios = pd.read_csv(
    'TA_PRECOS_MEDICAMENTOS.csv', 
    delimiter="|", 
    decimal=",", 
    encoding="latin1",
    header=None,
    error_bad_lines=False,
    low_memory=False)


# Head dos 5 primeiros registro da tabela com todos as colunas 

# In[2]:


remedios.head(5)


# <b>número e nome das colunas <b>

# In[3]:


remedios.iloc[0]


# In[4]:


remedios.columns


# In[5]:


remediosA = pd.DataFrame(remedios,columns=[5,8,9,14,15])
remediosA.columns = ['Nome do produto', 'Substância', 'Tipo de medicamento','NU_PF0_INTEIRO','NU_PF18_INTEIRO']


# Tabela reduzida a: <b>nome do produto, Nome da Substância, Tipo do produto, preço Fábrica de teto permitido para a comercialização com isenção do imposto de ICMS e preço Fábrica de teto permitido para a comercialização sem isenção do imposto de
# ICMS.   <b>

# In[6]:


remediosA.head(8)


# In[9]:


listaNomes = remediosA['Nome do produto'].unique()
listaSubstancia = remediosA['Substância'].unique()

print(listaNomes,listaSubstancia)


# <H2><i> quantidade de medicamentos fitoterápicos registrados<i></H2>

# In[16]:


fitoterapicos = remediosA[(remediosA['Tipo de medicamento']=='9')]
len(fitoterapicos['Nome do produto'].unique())


# In[17]:


fitoterapicos.head(7)


# <H2><i> quantidade de radiofármacos registrados <i></H2>

# In[12]:


radiofarmacos = remediosA[(remediosA['Tipo de medicamento']=='10')]
len(radiofarmacos['Nome do produto'].unique())


# In[13]:


radiofarmacos.head()


# <H2><i> quantidade de Genéricos registrados <i></H2>

# In[26]:


genericos = remediosA[(remediosA['Tipo de medicamento']=='1')]
len(genericos['Nome do produto'].unique())


# In[33]:


genericos.head(10)


# In[34]:


tiposderemedio = ['GENÉRICO','PATENTE', 'REFERÊNCIA', 'SIMILAR', 'NOVO', 'ESPECÍFICO', 'BIOLÓGICOS','DINAMIZADO','FITOTERÁPICO' , 'RADIOFÁRMACO', 'BIOLÓGICOS NOVOS']


# <h3><b> Tipos de medicamentos<b></h3> <h4>Iniciando a renomeação da coluna 10 'Tipo de medicamento' </h4>

# In[35]:


tiposderemedio


# In[36]:


remediosA['nome do tipo']=tiposderemedio[(remediosA['Tipo de medicamento']=='1')]


# In[39]:


remediosA.head(7)

