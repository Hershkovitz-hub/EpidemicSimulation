import pymunk

space = pymunk.Space()
space.gravity = 0, -100

body = pymunk.Body(1, 1666)
body.position = 50, 100

poly = pymunk.Poly.create_box(body)
space.add(body, poly)

print_options = pymunk.SpaceDebugDrawOptions()

while True:
    space.step(0.02)
    space.debug_draw(print_options)
