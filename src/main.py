import argparse
from generator.file_generator import FileGenerator
from loader.config_loader import ConfigLoader
from models.robot import Robot

def parse_args():
    parser = argparse.ArgumentParser(description="Generate XML files for robot parts")
    parser.add_argument("--config", required=True, help="Path to the configuration files.")
    return parser.parse_args()

def main():
    args = parse_args()

    robot_info = ConfigLoader.load_config('general.json')
    part_info = ConfigLoader.load_config('par.json')

    file_generator = FileGenerator(config_path=args.config)
    
    for robot_type, robot_list in robot_info.items():
        for robot_data in robot_list:
            robot = Robot(robot_data['robotName'], robot_data['robotVersion'], robot_data["parts"])
            part_data = {part: part_info[part] for part in robot.parts if part in part_info}
            file_generator.generate_files_for_robot(robot, part_data)

if __name__ == "__main__":
    main()
