import os
import shutil

# Target directory path
path = r'E:\Entertainment\steamapps\common\Barotrauma\LocalMods\Hungry Europans Russian Localisation'

# Source files
source_dir = os.path.dirname(os.path.abspath(__file__))
russian_xml_source = os.path.join(source_dir, 'Content', 'Texts', 'Russian', 'Russian.xml')
filelist_xml_source = os.path.join(source_dir, 'filelist.xml')

def build_mod():
    """Build the mod by copying files to the target directory"""
    try:
        # Check if target directory exists, if not create it
        if not os.path.exists(path):
            print(f"Creating directory: {path}")
            os.makedirs(path)
        else:
            print(f"Directory already exists: {path}")
        
        # Create Content subdirectory
        content_dir = os.path.join(path, 'Content')
        if not os.path.exists(content_dir):
            print(f"Creating Content directory: {content_dir}")
            os.makedirs(content_dir)
        
        # Create Text subdirectory inside Content
        text_dir = os.path.join(content_dir, 'Texts')
        if not os.path.exists(text_dir):
            print(f"Creating Texts directory: {text_dir}")
            os.makedirs(text_dir)
        
        # Create Russian subdirectory inside Text
        russian_dir = os.path.join(text_dir, 'Russian')
        if not os.path.exists(russian_dir):
            print(f"Creating Russian directory: {russian_dir}")
            os.makedirs(russian_dir)
        
        # Copy Russian.xml file
        russian_xml_target = os.path.join(russian_dir, 'Russian.xml')
        if os.path.exists(russian_xml_source):
            print(f"Copying Russian.xml from {russian_xml_source} to {russian_xml_target}")
            shutil.copy2(russian_xml_source, russian_xml_target)
            print("Russian.xml copied successfully")
        else:
            print(f"Warning: Source file not found: {russian_xml_source}")
        
        # Copy filelist.xml to root directory
        filelist_xml_target = os.path.join(path, 'filelist.xml')
        if os.path.exists(filelist_xml_source):
            print(f"Copying filelist.xml from {filelist_xml_source} to {filelist_xml_target}")
            shutil.copy2(filelist_xml_source, filelist_xml_target)
            print("filelist.xml copied successfully")
        else:
            print(f"Warning: Source file not found: {filelist_xml_source}")
        
        print("\nMod build completed successfully!")
        print(f"Target directory: {path}")
        
    except Exception as e:
        print(f"Error during mod build: {str(e)}")
        return False
    
    return True

if __name__ == '__main__':
    build_mod()