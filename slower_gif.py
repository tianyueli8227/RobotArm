from PIL import Image, ImageSequence

def slow_down_gif(input_path, output_path, slowdown_factor):

    with Image.open(input_path) as img:
        new_frames = []
        for frame in ImageSequence.Iterator(img):
            new_frame = frame.copy()
            new_frames.append(new_frame)
        new_frames[0].save(output_path, save_all=True, append_images=new_frames[1:], loop=0, duration=img.info['duration'] * slowdown_factor)

# Example usage
slow_down_gif('lift.gif', 'slowed_down.gif', 8)
