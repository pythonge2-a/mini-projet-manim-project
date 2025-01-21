import os
import uuid


# Function to generate video from a user manim script
def generate_manim_video(code):
    # Generate unique ID for this video
    video_id = str(uuid.uuid4())
    temp_script = f'temp_{video_id}.py'
    output_name = f'output_{video_id}'

    # save script in a temp file
    with open(temp_script, 'w') as f:
        f.write(code)
        
    # generate the video with manim
    os.system(f"manim -qh {temp_script} -o " + output_name)

    # delete temp file
    os.remove(temp_script)

    return video_id


# Function to generate video from a pre-coded manim script with parameters
def generate_pre_coded_video(script_name, **kwargs):
    # Generate unique ID
    video_id = str(uuid.uuid4())
    output_name = f'{video_id}'
    
    # Construct command with script name and output
    command = f"python {script_name} --output_name {output_name}"
    
    # Add additional parameters
    for key, value in kwargs.items():
        command += f" --{key} {value}"
    
    # Execute command
    os.system(command)

    return video_id