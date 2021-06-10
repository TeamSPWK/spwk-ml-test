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

`spaces`
- Space samples to place patches. 
- It consists of several spaces

`space`
- dictionary of two items
    - shell : coordinate array of polygon shell
    - holes : list containing coordinate array of polygon hole

`patch`
- coordinate array of patch to fill space
- fixed value
- [[-2.5, -1.15], [2.5, -1.15], [2.5, 1.15], [-2.5, 1.15], [-2.5, -1.15]]

`placed_patches`
- list containing coordinate array of placed patches

Methods

`select_space(index)`
`step(patch_x, patch_y, patch_angle)`
`reset()`

With the code below, you can check how the environment works
```python
from spwkml import PolygonFillEnv

env = PolygonFillEnv()

print(env.spaces)
print(env.space)
print(env.patch)

for i in range(len(env.spaces)):
    env.select_space(i)
    print(env.space)
    env.render()

env.select_space(5)
env.render()

state = env.step(5,5,-1)
print(state)
env.render()

state = env.step(4,4,-0.8)
print(state)
env.render()

state = env.step(4,3,-0.8)
print(state)
env.render()

state = env.step(-4,-4,-0.8)
print(state)
env.render()
```