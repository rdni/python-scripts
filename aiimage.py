from diffusers import AutoPipelineForText2Image
import torch
import os
import random

pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float32)

prompt = "A cinematic shot of a computer with code on it."

output = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0)

random_string = "".join(random.choices("12344567890", k=8))

output_file = os.path.join(os.path.join(os.getcwd(), "output"), f"{random_string}.jpg")

output.images[0].save(output_file)