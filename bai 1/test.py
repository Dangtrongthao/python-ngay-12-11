name1='thao'
name2='linh'

comparer=set(name1) &set(name2)
le=len(comparer)
kq=''
if le>=3:
    kq=' rat hop'
elif  le>0 &le<3:

    kq= 'hop'
elif le==0:
    kq='ko hop'

