# Reto de Compiladores

El codigo presentado define una gramática que nos permite realizar distinas funcionalidades, sin el uso de operadores de python. Al definir nuestra gramática somos capaces de resolver problemas de asignación, sumas, restas, multiplicaciones, divisiones y muchas más. Ademas de que somos capaces de acceder a funciones de opencv y a algunas de numpy. Y por ultimo una funcionalidad que le agrega mucho valor es la implementación de flujos, con esto nos referimos a que podemos concatenar algunas funciones y obtener un resultado correcto al final.

### Como correr el sistema

Para correr el sistema es necesario seguir los siguientes pasos:

1. Tener python instalado en tu computadora.
2. Instalar numpy, matplotlib, opencv, ply y networkx. A traves de el manejador de paquetes pip.
3. En la terminal correr el comando: python lexer.py
4. Al correr este comando el sistema te preguntara si quieres que se lea un archivo o no. Si decides la opción de leer un archivo solo le necesitas pasar el path del mismo, para que el sistema lo pueda leer. De lo contrario aparecera seras capaz de ingresar cualquier input que quieras al sistema y recibiras un resultado.

### Pruebas Manuales de La Gramática

1) Suma

Para la suma hacemos una prueba simple de 1+1, cuyo resultado debería ser 2. A continuación anexamos 1 foto del árbol generado y otra que demuestra el resultado de la operación.

- Árbol

![1+1](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/b45fc49c-bad2-47e6-8b4d-116e7badbc50)

- Resultado

<img width="353" alt="Screenshot 2024-04-28 at 11 39 43 p m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/246437c3-ada2-4cd0-a060-d5a613453750">

2) Resta

Para la resta hacemos una prueba simple de 5-8, cuyo resultado debería ser -3. A continuación anexamos 1 foto del árbol generado y otra que demuestra el resultado de la operación.

- Árbol

![5-8](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/bdad6eca-91cc-44d6-a13d-dccc6a3b1ad1)

- Resultado

<img width="353" alt="Screenshot 2024-04-28 at 11 41 58 p m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/a5c26758-9e93-445f-a771-2db8f52aaf4b">


3) Multiplicación

Para la multiplicación hacemos una prueba simple de 5*5, cuyo resultado debería ser 25. A continuación anexamos 1 foto del árbol generado y otra que demuestra el resultado de la operación.

- Árbol

![5*5](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/020c9da3-a1a8-4f7f-8d18-14f3ee7429dc)

- Resultado

<img width="315" alt="Screenshot 2024-04-28 at 11 44 06 p m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/aff3041a-288d-496e-88b3-a015fe35a32b">

4) División

Para la división hacemos una prueba simple de 16/2, cuyo resultado debería ser 8. A continuación anexamos 1 foto del árbol generado y otra que demuestra el resultado de la operación.

- Árbol

![16:2](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/bed3e709-b8e6-49e7-91b4-c8a440f92090)

- Resultado

<img width="363" alt="Screenshot 2024-04-28 at 11 45 44 p m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/c1641ee9-88fb-4287-bac3-9d768b3df2d1">

5) Exponentes

Para el exponente hacemos una prueba simple de 4^2, cuyo resultado debería ser 16.  A continuación anexamos 1 foto del árbol generado y otra que demuestra el resultado de la operación.

- Árbol

![4^2](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/d413fe7b-24e0-4fc1-8d32-d5192488a28f)

- Resultado

<img width="364" alt="Screenshot 2024-04-28 at 11 46 46 p m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/5edc4ba5-9f03-46c4-a205-a8e5e5509422">

6) PEMDAS

Para las operaciones PEMDAS hacemos una prueba simple de 5+8*2/(6+2), cuyo resultado debería ser 7.  A continuación anexamos 1 foto del árbol generado y otra que demuestra el resultado de la operación.

- Árbol

![PEMDAS](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/6577f102-73b6-4b08-b1b9-1f5067883793)

- Resultado

<img width="473" alt="Screenshot 2024-04-28 at 11 49 05 p m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/12f823c6-97e9-4763-8196-3d790992b286">

7) Asignación de Variables

Para las asignación de variables hacemos una prueba simple de a = "hola", cuyo resultado debería ser que a ahora toma el valor de "hola".  A continuación anexamos 1 foto del árbol generado y otra que demuestra el resultado de la operación.

- Árbol

![a=hola](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/f5261925-d9b2-4f02-97f6-d7608cd00807)

- Resultado

<img width="430" alt="Screenshot 2024-04-28 at 11 51 34 p m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/14536772-3456-4e43-8eff-dacd02fca97b">

8) Flujos

Para los flujos haremos una demostración con las funciones load_image(), gen_vector(), blur() y show_image(). En esta prueba se observa como en vez de tener una función muy grande que recibe muchos parametros, el resultado de una pasa a la siguiente hasta llegar a un resultado. A continuación presentamos los árboles generados y la imágen del principio y del final.

- Árboles

  - img = load_image()

    ![flujo_1](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/9d8e0195-ba7f-4316-bef9-177740b234b8)

  - size = gen_vector()

    ![flujo_@](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/8c6d2ae7-3f1e-4b5e-bfac-97ecc854f669)

  - img2 = img -> blur(size) -> blur(size) -> blur(size)

    ![flujo_3](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/6cc336df-bf84-493a-8095-7dfd1de59734)

- Resultado

  - Imágen Inicial

    ![cr7](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/7b5d54a5-1482-418d-b995-067cd20020bb)

  - Imágen Final
  
    <img width="1511" alt="Screenshot 2024-04-29 at 12 01 34 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/a5ea9887-a751-43f3-b3e4-9af6350cf974">

### Funcionalidades implementadas

El profesor nos dio la opción de realizar diferentes actividades a nuestro codigo. A continuación presentamos las que hicimos, y adjuntamos pruebas de que estas funcionan.

1) Aceptar archivos y Ejecutar el contenido.

Para esta funcionalidad al correr nuestro programa se le pide al usuario el nombre del archivo que quiere correr. Si el usuario esto desea ingresa el nombre y se corre todo el contenido. A continuación presentamos una prueba de como funciona. El resultado de nuestro archivo buscamos que sea 8.

- Archivo

<img width="118" alt="Screenshot 2024-04-29 at 12 14 22 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/6c7f66e7-a410-42e4-8dd6-f4658116f1a0">

- Árboles

  - a = 1+1
 
    ![a=1+1](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/db93a677-4bea-4ca7-952d-360ea9d9d546)

  - b = 2+2

    ![b=2+2](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/3bb7a3f8-60b7-43ff-9c75-dd35f128e6ac)

  - c = 2

    ![c=2](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/f94c8725-42c7-4bca-ba38-173408060a27)

  - d = c+a+b

    ![d=c+a+b](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/a65b865b-b40c-4638-9a6b-a4934781d42d)

  - d

    ![d](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/0c49be0e-c9f9-4f5c-b278-7877872240be)

- Resultados

  - a = 1+1
 
    <img width="953" alt="Screenshot 2024-04-29 at 12 19 05 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/288823df-65f8-419c-8ec2-ca6812bc86af">

  - b = 2+2
  
    <img width="419" alt="Screenshot 2024-04-29 at 12 21 00 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/75418741-bbba-424f-8d89-84700ecaddee">

  - c = 2

    <img width="442" alt="Screenshot 2024-04-29 at 12 21 31 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/388376f8-c804-4267-b49a-e14ed977a84a">

  - d = c+a+B

    <img width="369" alt="Screenshot 2024-04-29 at 12 22 06 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/0a3b7d91-54ed-48f7-b8c4-3999eaee77f5">

  - d

    <img width="307" alt="Screenshot 2024-04-29 at 12 22 21 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/ca459b1a-28ec-4614-8c63-9d3cd934ac32">


2) Aceptar 9 funciones de numpy.

Implementamos 9 funciones de numpy para nuestra grámatica. Todas caen en el ámbito trigonométrico. A continuación presentamos todas con pruebas de su funcionamiento.

- numpy_sin(20): El seno de 20 es 0.9129, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![sin](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/07e87929-a150-4faa-9668-6d01c20271c5)

  - Resultado

    <img width="416" alt="Screenshot 2024-04-29 at 12 26 08 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/5bdeee98-2b14-4600-83ba-775d240a279c">

- numpy_cos(20): El coseno de 20 es 0.4080, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![cos](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/451db6a8-bb8a-4d64-a102-d7efdde7ef88)

  - Resultado

    <img width="386" alt="Screenshot 2024-04-29 at 12 27 50 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/9822670e-92c1-4c63-b10f-b5d577957149">

- numpy_tan(20): La tangente de 20 es 2,2371, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![tan](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/02d5ae5d-7c02-4406-9ca7-dc1eebba9b43)

  - Resultado
 
    <img width="420" alt="Screenshot 2024-04-29 at 12 29 18 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/37166088-67ae-4c8d-875c-ffe33c5a77ea">

- numpy_arcsin(0.5): El arcoseno de 0.5 es 0.5235, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![arcsin](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/ec696e22-4983-44ea-a095-12be63ece358)

  - Resultado

    <img width="400" alt="Screenshot 2024-04-29 at 12 31 58 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/497a9e65-9307-4d89-8a7b-f8819837802d">

- numpy_arccos(0.5): El arcocoseno de 0.5 es 1.0471, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![arccos](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/e2e3d134-42c9-445f-90bb-21f5679102bd)

  - Resultado

   <img width="419" alt="Screenshot 2024-04-29 at 12 33 49 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/69d6da02-7e8a-437c-8c65-f1179d1cd442">

- numpy_arctan(0.5): El arcotangente de 0.5 es 0.4636, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![arctan](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/2d8057a3-7704-446f-a862-888c4d721333)

  - Resultado
 
    <img width="439" alt="Screenshot 2024-04-29 at 12 35 14 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/5ff5c609-2dc7-4b5d-a9cf-f8d99835b0ac">

- numpy_sinh(2): El seno hiperbólico de 2 es 3.6268, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![sinh](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/6c8f745d-31af-4f5d-bf5d-e7228fc7cb6d)

  - Resultado

    <img width="435" alt="Screenshot 2024-04-29 at 12 36 46 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/33acc240-a136-4be9-b998-311a33c45fe5">

- numpy_cosh(2): El coseno hiperbólico de 2 es 3.7621, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![cosh](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/b5f67fc4-6257-4717-913e-2468fed82042)

  - Resultado
 
    <img width="391" alt="Screenshot 2024-04-29 at 12 38 12 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/cb6f5c70-7e11-4cc7-b86a-39ac6fd51473">

- numpy_tanh(2): La tangente hiperbólico de 2 es 0.9640, a continuación adjuntamos pruebas del funcionamiento.

  - Árbol

    ![tanh](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/8506e269-51ed-4f87-9f40-9ccf6321034f)

  - Resultado
 
    <img width="409" alt="Screenshot 2024-04-29 at 12 39 48 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/50005feb-3d7c-4dc7-bef6-549e926d7811">

3) Implementación de visualización de histogramas con opencv.

Esta función nos permite pasar una imagen y enseñamos un histograma que muestra como varia cada uno de los tres canales (rgb) en la imagen. A continuación presentamos el árbol generado al realizar esta operación, como la imagen del histograma generado.

- Árbol

![hv](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/b5abd222-38f9-478d-b594-a885df148364)

- Resultado

![hrgb](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/6eb51632-095a-4e61-bf88-e23c8448d1e7)


4) Implementación de un algoritmo complejo como herramienta en el lenguaje: WaterShed, Grabcut, TemplateMatching, CannyEdgeDetection.

En esta función se implementa el algoritmo grabcut. Al cual le pasamos una imagen que posee dos propiedades. Una es la imagen completa y la otra es una imagen que tiene líneas que delimitan lo que queremos cortar. Al pasar esta imagen por este algoritmo de opencv somos capaces de hacer la correcta segmentación de la imagen. Usamos unas transformaciones y lo pasamos por la función grabCut() de opencv, al final devolvemos una imagen que hace la segmentación correcta. A continuación presentamos el árbol generado, la imagen inicial y la final.

- Árbol

![grabcut](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/c69e474b-9c5d-4e47-97cd-bd491bbf7b40)

- Resultado

  - Imagen Inicial

    ![random_guy](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/4235c18a-ba1e-4b0e-8058-abab1a245f44)

  - Imagen Final
 
    <img width="722" alt="Screenshot 2024-04-29 at 12 47 42 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/2899faa3-696c-451a-b200-adfd08800377">

5) Aceptar None como valor de la gramática para inicialización de variables. A continuación presentamos pruebas del funcionamiento.

- Árbol

![None](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/ec73299f-181f-4417-80c8-bf192bb709b3)

- Resultado

<img width="381" alt="Screenshot 2024-04-29 at 12 51 03 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/be29a116-db68-4d1c-a0c0-5efce5322a04">

6) Exportación del árbol de sintaxis abstracto como texto incluyendo las matrices generadas. A continuación presentamos el árbol generado por la operación 5+8*2/(6+2), y enseñaremos como resultado la traducción que hace nuestro programa para exportar el árbol a un archivo.

- Árbol

![PEMDAS](https://github.com/DiegoAraque21/compiler_reto/assets/84464594/6577f102-73b6-4b08-b1b9-1f5067883793)

- Resultado

<img width="481" alt="Screenshot 2024-04-29 at 12 54 13 a m" src="https://github.com/DiegoAraque21/compiler_reto/assets/84464594/e4f999c8-14b6-4f13-999c-dc627329bd6c">

