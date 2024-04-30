# Reto de Compiladores

El codigo presentado define una gramática que nos permite realizar distinas funcionalidades, sin el uso de operadores de python. Al definir nuestra gramática somos capaces de resolver problemas de asignación, sumas, restas, multiplicaciones, divisiones y muchas más. Ademas de que somos capaces de acceder a funciones de opencv y a algunas de numpy. Y por ultimo una funcionalidad que le agrega mucho valor es la implementación de flujos, con esto nos referimos a que podemos concatenar algunas funciones y obtener un resultado correcto al final.

### Como correr el sistema

Para correr el sistema es necesario seguir los siguientes pasos:

1. Tener python instalado en tu computadora.
2. Instalar numpy, matplotlib, opencv, ply y networkx. A traves de el manejador de paquetes pip.
3. En la terminal correr el comando: python lexer.py
4. Al correr este comando el sistema te preguntara si quieres que se lea un archivo o no. Si decides la opción de leer un archivo solo le necesitas pasar el path del mismo, para que el sistema lo pueda leer. De lo contrario aparecera seras capaz de ingresar cualquier input que quieras al sistema y recibiras un resultado.

### Pruebas Manuales de La Gramática

Para realizar estas pruebas se puede correr el archivo test.txt que se encuentra en el repo, y recibiras los mismo resultados.

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
