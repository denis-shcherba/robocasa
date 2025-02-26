#!/usr/bin/env python3
import mujoco
import mujoco.viewer
import numpy as np
import time
import os

def view_mujoco_xml(xml_path):
    """
    Load and visualize a MuJoCo XML file in an interactive window
    
    Args:
        xml_path (str): Path to the XML file to visualize
    """
    if not os.path.exists(xml_path):
        print(f"Error: File {xml_path} not found")
        return
    
    try:
        model = mujoco.MjModel.from_xml_path(xml_path)
        data = mujoco.MjData(model)
        
        print(f"Model loaded successfully from {xml_path}")
        print(f"Number of bodies: {model.nbody}")
        print(f"Number of joints: {model.njnt}")
        print(f"Number of actuators: {model.nu}")
        
        print("Starting interactive viewer. Close the window to exit.")
        mujoco.viewer.launch(model, data)
        
    except Exception as e:
        print(f"Error loading or visualizing the model: {e}")

if __name__ == "__main__":
    xml_path = "../kitchen_dataset/INDUSTRIAL_ONE_WALL_SMALL.xml"
    view_mujoco_xml(xml_path)