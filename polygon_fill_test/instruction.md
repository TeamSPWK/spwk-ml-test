<h1 align="center">Polygon Fill Test</h1>

<p align="center">
  <a href="#problem-definition">Problem Definition</a> •
  <a href="#manual">Manual</a>
</p>

<h2 align="center">Problem Definition</h2>

<h2 align="center">Manual</h2>

`spwkml` package offers environment class for problem definition above.  
You can make environment instance with it.

```python
from spwkml import PolygonFillEnv

env = PolygonFillEnv()
```

`PolygonFillEnv` class has several properties and methods.

Properties

`env.spaces`
- Space samples to place patches. 
- It consists of several spaces

`env.space`
- dictionary of two items
    - shell : coordinate array of polygon shell
    - holes : list containing coordinate array of polygon hole

`env.patch`
- coordinate array of patch to fill space
- fixed value
- [[-2.5, -1.15], [2.5, -1.15], [2.5, 1.15], [-2.5, 1.15], [-2.5, -1.15]]

`env.placed_patches`
- list containing coordinate array of placed patches

Methods

`env.select_space(index)`
`env.step(patch_x, patch_y, patch_angle)`
`env.reset()`

With the code below, you can check how the environment works

First, with `env.spaces` property, you can get information of predefined spaces.  
There are 10 predefined spaces.

```python
print(env.spaces)

[
    {
        'shell': array([[-10., -10.],
                        [ 10., -10.],
                        [ 10.,  10.],
                        [-10.,  10.],
                        [-10., -10.]]), 
        'holes': []
    }, 
    {
        'shell': array([[-10., -10.],
                        [ -3., -10.],
                        [ -3.,  10.],
                        [-10.,  10.],
                        [-10., -10.]]), 
        'holes': []
    }, 
    {
        'shell': array([[-5., -5.],
                        [ 5., -5.],
                        [ 5.,  5.],
                        [-5.,  5.],
                        [-5., -5.]]), 
        'holes': []
    }, 
    {
        'shell': array([[-10., -10.],
                        [-10.,  10.],
                        [ 10.,  10.],
                        [ 10., -10.],
                        [-10., -10.]]), 
        'holes': [
            array([[-5., -5.],
                    [ 5., -5.],
                    [ 5.,  5.],
                    [-5.,  5.],
                    [-5., -5.]])
        ]
    }, 
    {
        'shell': array([[  0., -10.],
                        [ 10.,   0.],
                        [  0.,  10.],
                        [-10.,   0.],
                        [  0., -10.]]), 
        'holes': []
    }, 
    {
        'shell': array([[  0., -10.],
                        [-10.,   0.],
                        [  0.,  10.],
                        [ 10.,   0.],
                        [  0., -10.]]), 
        'holes': [
            array([[ 0., -3.],
                    [ 3.,  0.],
                    [ 0.,  3.],
                    [-3.,  0.],
                    [ 0., -3.]])
        ]
    }, 
    {
        'shell': array([[-10., -10.],
                        [ 10., -10.],
                        [ 10.,  -6.],
                        [ -2.,  -6.],
                        [ -2.,   6.],
                        [ 10.,   6.],
                        [ 10.,  10.],
                        [-10.,  10.],
                        [-10., -10.]]), 
        'holes': []
    }, 
    {
        'shell': array([[-10., -10.],
                        [  8., -10.],
                        [ 10.,   7.],
                        [-10.,  10.],
                        [  0.,  -3.],
                        [-10., -10.]]), 
        'holes': []
    }, 
    {
        'shell': array([[-10., -10.],
                        [ 10., -10.],
                        [  0.,  10.],
                        [-10., -10.]]), 
        'holes': []
    }, 
    {
        'shell': array([[-10., -10.],
                        [  0.,  10.],
                        [ 10., -10.],
                        [-10., -10.]]), 
       'holes': [
            array([[-4., -6.],
                    [ 4., -4.],
                    [-2.,  2.],
                    [-4., -6.]])
        ]
    }
]
```

One of predefined spaces is selected as current space, and you can get this by `env.space` property.  
As default, first space (space of index 0) is selected as current space.  
```python
print(env.space)

{
    'shell': array([[-10., -10.],
                    [ 10., -10.],
                    [ 10.,  10.],
                    [-10.,  10.],
                    [-10., -10.]]), 
    'holes': []
}
```

You can get fixed patch information with `env.patch` property.
This is unit patch, and when you apply action, this patch will be rotated, and translated.
```python
print(env.patch)

array([[-2.5 , -1.15],
       [ 2.5 , -1.15],
       [ 2.5 ,  1.15],
       [-2.5 ,  1.15],
       [-2.5 , -1.15]])
```

In order to know the shape of predefined spaces, you can use `env.select_space(index)` method and `env.render` method.  
There are 10 predefined spaces, so you can use index 0~9 without adding other spaces.
```python
for i in range(len(env.spaces)):
    env.select_space(i)
    print(env.space)
    env.render()
```

You will apply some actions with `env.step()` method and see the result of it.
5th predifined space is good to know how it works, so, choose 5th space.  
It's diamond shape space with a hole in center.
```python
env.select_space(5)
env.render()
```
<img src="https://user-images.githubusercontent.com/39043516/121534337-17bc5880-ca3c-11eb-99a2-d1d4dba5f66c.png" alt="render" />

```python
state = env.step(0,0,0)
print(state)
env.render()

{
    'is_valid': False, 
    'n_patches': 0, 
    'space': {
        'shell': array([[  0., -10.],
                        [-10.,   0.],
                        [  0.,  10.],
                        [ 10.,   0.],
                        [  0., -10.]]), 
        'holes': [
            array([[ 0., -3.],
                    [ 3.,  0.],
                    [ 0.,  3.],
                    [-3.,  0.],
                    [ 0., -3.]])
        ]
    }, 
    'selected_patch': array([[-2.5 , -1.15],
                            [ 2.5 , -1.15],
                            [ 2.5 ,  1.15],
                            [-2.5 ,  1.15],
                            [-2.5 , -1.15]]), 
    'placed_patches': [], 
    'area_out_of_space': 10.654999999999998, 
    'area_intersect_patches': 0.0
}
```
<img src="https://user-images.githubusercontent.com/39043516/121534557-49352400-ca3c-11eb-9c29-6f9df338b57f.png" alt="render" />

```python
state = env.step(4,4,0)
print(state)
env.render()

{
    'is_valid': False, 
    'n_patches': 0, 
    'space': {
        'shell': array([[  0., -10.],
                        [-10.,   0.],
                        [  0.,  10.],
                        [ 10.,   0.],
                        [  0., -10.]]), 
        'holes': [
            array([[ 0., -3.],
                    [ 3.,  0.],
                    [ 0.,  3.],
                    [-3.,  0.],
                    [ 0., -3.]])
        ]
    }, 
    'selected_patch': array([[1.5 , 2.85],
                            [6.5 , 2.85],
                            [6.5 , 5.15],
                            [1.5 , 5.15],
                            [1.5 , 2.85]]),
    'placed_patches': [], 
    'area_out_of_space': 1.3612500000000005, 
    'area_intersect_patches': 0.0
}
```
<img src="https://user-images.githubusercontent.com/39043516/121534600-53efb900-ca3c-11eb-987f-47aed3a690a1.png" alt="render" />

```python
state = env.step(4,4,-0.8)
print(state)
env.render()

{
    'is_valid': True, 
    'n_patches': 1, 
    'space': {
        'shell': array([[  0., -10.],
                        [-10.,   0.],
                        [  0.,  10.],
                        [ 10.,   0.],
                        [  0., -10.]]), 
        'holes': [
            array([[ 0., -3.],
                    [ 3.,  0.],
                    [ 0.,  3.],
                    [-3.,  0.],
                    [ 0., -3.]])
        ]
    }, 
    'selected_patch': array([[1.43327372, 4.99217751],
                            [4.91680727, 1.40539706],
                            [6.56672628, 3.00782249],
                            [3.08319273, 6.59460294],
                            [1.43327372, 4.99217751]]),
    'placed_patches': [
        array([[1.43327372, 4.99217751],
                [4.91680727, 1.40539706],
                [6.56672628, 3.00782249],
                [3.08319273, 6.59460294],
                [1.43327372, 4.99217751]])
    ], 
    'area_out_of_space': 0.0, 
    'area_intersect_patches': 0.0
}
```
<img src="https://user-images.githubusercontent.com/39043516/121534679-6669f280-ca3c-11eb-9ede-ac5ae2ed156a.png" alt="render" />

```python
state = env.step(-2,-6,-0.8)
print(state)
env.render()

{
    'is_valid': True, 
    'n_patches': 2, 
    'space': {
        'shell': array([[  0., -10.],
                        [-10.,   0.],
                        [  0.,  10.],
                        [ 10.,   0.],
                        [  0., -10.]]), 
        'holes': [
            array([[ 0., -3.],
                    [ 3.,  0.],
                    [ 0.,  3.],
                    [-3.,  0.],
                    [ 0., -3.]])
        ]
    }, 
    'selected_patch': array([[-4.56672628, -5.00782249],
                            [-1.08319273, -8.59460294],
                            [ 0.56672628, -6.99217751],
                            [-2.91680727, -3.40539706],
                            [-4.56672628, -5.00782249]]),
    'placed_patches': [
        array([[1.43327372, 4.99217751],
                [4.91680727, 1.40539706],
                [6.56672628, 3.00782249],
                [3.08319273, 6.59460294],
                [1.43327372, 4.99217751]]), 
        array([[-4.56672628, -5.00782249],
                [-1.08319273, -8.59460294],
                [ 0.56672628, -6.99217751],
                [-2.91680727, -3.40539706],
                [-4.56672628, -5.00782249]])
    ], 
    'area_out_of_space': 0.0, 
    'area_intersect_patches': 0.0
}
```
<img src="https://user-images.githubusercontent.com/39043516/121534739-74b80e80-ca3c-11eb-94fc-d1572c0a2f0e.png" alt="render" />

```python
state = env.step(-4,-4,-0.8)
print(state)
env.render()

{
    'is_valid': False, 
    'n_patches': 2, 
    'space': {
        'shell': array([[  0., -10.],
                        [-10.,   0.],
                        [  0.,  10.],
                        [ 10.,   0.],
                        [  0., -10.]]), 
        'holes': [
            array([[ 0., -3.],
                    [ 3.,  0.],
                    [ 0.,  3.],
                    [-3.,  0.],
                    [ 0., -3.]])
        ]
    }, 
    'selected_patch': array([[-6.56672628, -3.00782249],
                            [-3.08319273, -6.59460294],
                            [-1.43327372, -4.99217751],
                            [-4.91680727, -1.40539706],
                            [-6.56672628, -3.00782249]]),
    'placed_patches': [
        array([[1.43327372, 4.99217751],
                [4.91680727, 1.40539706],
                [6.56672628, 3.00782249],
                [3.08319273, 6.59460294],
                [1.43327372, 4.99217751]]), 
        array([[-4.56672628, -5.00782249],
                [-1.08319273, -8.59460294],
                [ 0.56672628, -6.99217751],
                [-2.91680727, -3.40539706],
                [-4.56672628, -5.00782249]])
    ], 
    'area_out_of_space': 0.0, 
    'area_intersect_patches': 4.905615392546818
}
```
<img src="https://user-images.githubusercontent.com/39043516/121534763-7b468600-ca3c-11eb-96f4-51238e868629.png" alt="render" />

```python
state = env.step(-6,-2,-0.8)
print(state)
env.render()

{
    'is_valid': True, 
    'n_patches': 3, 
    'space': {
        'shell': array([[  0., -10.],
                        [-10.,   0.],
                        [  0.,  10.],
                        [ 10.,   0.],
                        [  0., -10.]]), 
        'holes': [
            array([[ 0., -3.],
                    [ 3.,  0.],
                    [ 0.,  3.],
                    [-3.,  0.],
                    [ 0., -3.]])
        ]
    }, 
    'selected_patch': array([[-8.56672628, -1.00782249],
                            [-5.08319273, -4.59460294],
                            [-3.43327372, -2.99217751],
                            [-6.91680727,  0.59460294],
                            [-8.56672628, -1.00782249]]),
    'placed_patches': [
        array([[1.43327372, 4.99217751],
            [4.91680727, 1.40539706],
            [6.56672628, 3.00782249],
            [3.08319273, 6.59460294],
            [1.43327372, 4.99217751]]), 
        array([[-4.56672628, -5.00782249],
            [-1.08319273, -8.59460294],
            [ 0.56672628, -6.99217751],
            [-2.91680727, -3.40539706],
            [-4.56672628, -5.00782249]]), 
        array([[-8.56672628, -1.00782249],
            [-5.08319273, -4.59460294],
            [-3.43327372, -2.99217751],
            [-6.91680727,  0.59460294],
            [-8.56672628, -1.00782249]])
    ], 
    'area_out_of_space': 0.0, 
    'area_intersect_patches': 0.0
}
```
<img src="https://user-images.githubusercontent.com/39043516/121534798-84cfee00-ca3c-11eb-9e1d-41d8ca4c717c.png" alt="render" />
