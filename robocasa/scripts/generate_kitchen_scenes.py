from robocasa.utils.env_utils import create_env
from robocasa.models.scenes.scene_registry import LayoutType, StyleType
from robocasa.utils.conversion import saveScene, remove_robot_elements
import os 

# Define the dataset directory
output_dir = "kitchen_dataset"

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for i, layout in enumerate(LayoutType):
    if i > 9: 
        break
    print(str(layout)[11:])  # Assuming you meant to slice the string representation
    for j, style in enumerate(StyleType):
        if j > 11 : 
            break
        env = create_env(
            env_name="Kitchen",
            layout_ids=[layout],
            style_ids=[style],
        )
        env.reset()
        xml_with_bot = saveScene(env)
        xml = remove_robot_elements(xml_with_bot)
        output_path = os.path.join(output_dir, f"{str(style)[10:]}_{str(layout)[11:]}.xml")
        
        with open(output_path, "w") as f:
            f.write(xml)
            print(f"Modified XML saved to: {output_path}")
        print(str(style)[10:])  # Assuming you meant to slice the string representation
