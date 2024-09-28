#globals
import cohere

urls={
'sports':['https://en.wikipedia.org/wiki/Mohamed_Salah','https://en.wikipedia.org/wiki/Cristiano_Ronaldo','https://en.wikipedia.org/wiki/Lionel_Messi'],
'history':['https://en.wikipedia.org/wiki/Napoleon','https://en.wikipedia.org/wiki/Adolf_Hitler','https://en.wikipedia.org/wiki/Tutankhamun'],
'science': ['https://en.wikipedia.org/wiki/Ahmed_Zewail','https://en.wikipedia.org/wiki/Magdi_Yacoub','https://en.wikipedia.org/wiki/Albert_Einstein']
}
co = cohere.Client('mNTuSN8C7gzvV5QMg2iND2Jr7JD2TYzK3un5ubgD')
MCQ={
    'A':'sports',
    'B':'history',
    'C':'science'
}
persons={
    'sports':['Mohamed Salah','Cristiano Ronaldo','Lionel Messi'],
    'history':['Napoleon','Adolf Hitler','Tutankhamun'],
    'science': ['Ahmed Zewail','Magdi Yacoub','Albert Einstein']
}

