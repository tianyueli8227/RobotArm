import sapien.core as sapien
import numpy as np
import imageio
import os
from transforms3d.euler import euler2quat

def main():
    engine = sapien.Engine()
    # renderer = sapien.SapienRenderer(offscreen=True)  # Enable offscreen rendering
    renderer = sapien.SapienRenderer() 
    engine.set_renderer(renderer)

    scene = engine.create_scene()
    scene.set_timestep(1 / 100.0)

    scene.add_ground(altitude=0)
    actor_builder = scene.create_actor_builder()
    actor_builder.add_box_collision(half_size=[0.5, 0.5, 0.5])
    actor_builder.add_box_visual(half_size=[0.5, 0.5, 0.5], color=[1., 0., 0.])
    box = actor_builder.build(name='box')
    box.set_pose(sapien.Pose(p=[0, 0, 13]))

    scene.set_ambient_light([0.5, 0.5, 0.5])
    scene.add_directional_light([0, 1, -1], [0.5, 0.5, 0.5])

    # camera = scene.add_mounted_camera('camera', box, sapien.Pose(), 800, 600, 0, 2.0, 0.1, 100)
    camera = scene.add_camera("camera", width=800, height=600,fovy=2, near=0.1, far=100)
    pitch = -np.arctan2(2, 6)
    quat = euler2quat(0, pitch, 0)
    camera.set_local_pose(sapien.Pose([-6, -3, 3], quat))  # Position the camera

    frames = []
    for i in range(100):  # Capture 100 frames
        scene.step()
        scene.update_render()
        camera.take_picture()
        rgba = camera.get_color_rgba()  # Get the rendered image
        frames.append((rgba[:, :, :3] * 255).astype(np.uint8))

    # Save the frames as a GIF
    gif_path = 'simulation.gif'
    imageio.mimsave(gif_path, frames, fps=30)

    print(f"GIF saved at {gif_path}")

if __name__ == '__main__':
    main()
