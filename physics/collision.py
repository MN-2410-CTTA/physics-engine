def resolve_ground_collision(body, ground_y, restitution=0.6):
    bottom = body.position.y + body.size[1]

    if bottom >= ground_y:
        body.position.y = ground_y - body.size[1]

        # Reflect motion by adjusting previous position
        velocity_y = body.position.y - body.previous_position.y
        body.previous_position.y = body.position.y + velocity_y * restitution 