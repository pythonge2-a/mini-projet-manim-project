import os

# Function to generate video from a user manim script
def generate_manim_video(code):
    # save script in a temp file
    with open('temp.py', 'w') as f:
        f.write(code)
        
    # generate the video with manim
    os.system("manim -qh temp.py output")

    # delete temp file
    os.system("rm temp.py")

    return True


# Function to generate video from a pre-coded manim script with parameters
def generate_pre_coded_video(script_name, **kwargs):
    # Construct the command with the script name
    command = f"python {script_name}"
    
    # Add the additional parameters to the command
    for key, value in kwargs.items():
        command += f" --{key} {value}"
    
    # Execute the command
    os.system(command)

    return True


