# StringProcessing

Este projeto visa fazer uma análise de desempenho de alguns métodos de processamento de strings presentes na literatura. Sendo eles:

  - [Força Bruta](algoritmos/forca_bruta.py)
  - [Boyer-Moore-Horspool](algoritmos/bmh.py)
  - [Boyer-Moore-Horspool-Sunday](algoritmos/bmhs.py)
  - [Shift-And](algoritmos/shift_and.py) 
  - [Shift-And Aproximado](algoritmos/shift_and_aprox.py)
  
De posse desses algorimos, foram realizados sucessivos testes que levaram em consideração tamanho de entrada, tamanho do texto de busca, e tempo de execução. As figuras a seguir representam os resultados obtidos.

### Buscando pelo padrão "justo"

![](figuras/figura8-1(justo).png)
![](figuras/figura8-3(justo).png)

### Buscando pelo padrão "ipsum ultrices"

![](figuras/figura10-1(ipsum%20ultrices).png)
![](figuras/figura10-3(ipsum%20ultrices).png)

### Buscando pelo padrão "Quisque eget ligula in tortor commodo"

![](figuras/figura9-1(Quisque%20eget%20ligula%20in%20tortor%20commodo).png)
![](figuras/figura9-3(Quisque%20eget%20ligula%20in%20tortor%20commodo).png)


Mais detalhes sobre os testes e conclusões podem ser achados no [artigo](artigo.pdf) disponível no repositório.

#### [ Eduardo Cardoso ]
