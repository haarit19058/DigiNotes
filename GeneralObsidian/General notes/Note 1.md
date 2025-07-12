```python
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr) // 2
        left=merge_sort(arr[:mid])
        right=merge_sort(arr[mid:])
        arr=merge(left, right)
    return arr

def merge(left,right):
    i=0
    j=0
    merged=[]
    while i<len(left) and j<len(right):
        if left[i][0]<right[j][0]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    while i<len(left):
        merged.append(left[i])
        i += 1
    while j<len(right):
        merged.append(right[j])
        j += 1
    return merged

friends=int(input())
times=[]
for i in range(friends):
    times.append(list(map(int,input().split())))
times=merge_sort(times)
counter=0
i=0
j=0
counter=0
curr=0
while j < friends:
    if times[i][1]>=times[j][0]:
        curr+=1
        counter=max(counter,curr)
        j+=1
    else:
        curr=0
        i+=1
    

print(counter)
```





Abstract

  
Piezoelectric sensors operate based on the principle of the piezoelectric effect, which is the ability of certain materials to generate an electric charge in response to mechanical stress or deformation. Conversely, they can also undergo mechanical deformation in response to an applied electric field.
The aim of the experiment is to find the resonance frequency of the sensor. To do so the piezo is placed on the top of the speaker and then input with different frequencies are givven tto the speaker so the speaker vibrates at different frequencies ant the pizo works acccordingly. We use dso to record the output voltage of the sensor and the supplied frequency and he=nce at the resonance frequency the output voltage is maximized. we can easily see it in the outpt



Results 

on incresing the frequency oft he piezo electric sensor there were three peaks in the output voltage the maximu one occeured at 2350Hz and the coresponding output voltage is 2.08V . This is the resonance frequency of the piezoelectric sensor where the output voltage was the maximum than regular redings








Results 
The experiment showed that Sample 1 had the highest rate of methylene blue (MB) degradation. This was because it was stirred with magnetic beads, exposed to light, and contained Fe3O4 nanoparticles. Sample 2, with only light exposure and nanoparticles but no stirring, degraded MB more slowly than Sample 1. Sample 3, which lacked both light and nanoparticles, showed minimal MB degradation, acting as a control.

Another experiment analyzed MB degradation by measuring absorbance after dilution. Plotting absorbance against concentration helped to find epsilon using Beer-Lambert law equation. Plotting log(C0/C), where C0 is the initial MB concentration and C is the concentration after degradation.





Results 

I see. You want me to rewrite your observations using “we” instead of “I”. Here is one possible way to do that:

Distilled Water (H2O):
We didn’t notice much hydrogen gas after applying electricity to distilled water for 15 minutes. That’s expected, because distilled water is very pure and has hardly any ions (H+ and OH-) in it. Without enough ions, electricity can’t flow well. 

Tap Water:
We saw a few bubbles of hydrogen gas. Tap water has some minerals and ions in it.  So, it can carry some electricity, but not enough to make a lot of electrolysis and hydrogen gas. 

NaCl Solution:
We saw a lot of bubbles of hydrogen gas. Sodium chloride (NaCl) breaks up into Na+ and Cl- ions when it dissolves in water. These ions help electricity flow better, so electrolysis happens faster. The bubbles came out quickly at first, because there were many ions in the solution. But as the reaction went on, the number of ions reduces, so the rate of reaction also decreases. 

MgCl2 Solution:
We saw even more bubbles of hydrogen gas than with NaCl solution. Magnesium chloride (MgCl2) breaks up into Mg2+ and 2Cl- ions when it dissolves in water, giving more ions than NaCl and the charge is also +2. More ions and charge leads to higher rate of reaction. The reaction rate was fast at start and slowly decreased due to the same reason as NaCl i.e. the the concentration of ions decreases.
