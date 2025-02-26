import xml.etree.ElementTree as ET

def saveScene(env):

    xml_string = env.sim.model.get_xml()

    return xml_string

def remove_robot_elements(xml_string):
    """
    Parse an XML string and remove any elements with names containing 'gripper', 'robot', or 'mobilebase'.
    
    Args:
        xml_string (str): XML string representation of the environment
    
    Returns:
        str: Modified XML string with robot elements removed
    """
    # Parse the XML from string
    parser = ET.XMLParser()
    root = ET.fromstring(xml_string, parser)
    
    # Find all elements that match the patterns
    patterns = ['gripper', 'robot', 'mobilebase']
    elements_to_remove = []
    
    def find_matching_elements(element, parent=None):
        # Check if the current element's name contains any of the patterns
        for pattern in patterns:
            if pattern in element.tag.lower() or (element.get('name') and pattern in element.get('name').lower()):
                elements_to_remove.append((element, parent))
                break
        
        # Recursively check all children
        for child in list(element):
            find_matching_elements(child, element)
    
    # Start recursive search from root
    for child in list(root):
        find_matching_elements(child, root)
    
    # Remove the identified elements (in reverse order to avoid index issues)
    for element, parent in reversed(elements_to_remove):
        if parent is not None:
            parent.remove(element)
    
    # Convert back to string
    modified_xml = ET.tostring(root, encoding='unicode')
    
    return modified_xml

