from project import HeavyHardware
from project import PowerHardware
from project import ExpressSoftware
from project import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod # extract in a different func to avoid code repeat
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)

            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return 'Hardware does not exist'
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)

            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return 'Hardware does not exist'
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]

            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        hardware_total_memory = sum([device.memory for device in System._hardware])
        software_memory_consumption = sum([device.memory_consumption for device in System._software])

        hardware_total_capacity = sum([device.capacity for device in System._hardware])
        software_capacity_consumption = sum([device.capacity_consumption for device in System._software])

        result = 'System Analysis\n'\
                 + f'Hardware Components: {len(System._hardware)}\n'\
                 + f'Software Components: {len(System._software)}\n'\
                 + f'Total Operational Memory: {software_memory_consumption} / {hardware_total_memory}\n'\
                 + f'Total Capacity Taken: {software_capacity_consumption} / {hardware_total_capacity}'

        return result

    @staticmethod
    def system_split():
        result_list = []

        for hardware in System._hardware:
            express_software = [software for software in hardware.software_components if
                                isinstance(software, ExpressSoftware)]
            light_software = [software for software in hardware.software_components if
                              isinstance(software, LightSoftware)]
            total_software = [software.name for software in hardware.software_components]

            total_used_memory = sum([software.memory_consumption for software in hardware.software_components])
            total_used_capacity = sum([software.capacity_consumption for software in hardware.software_components])

            result = f'Hardware Component - {hardware.name}\n' \
                     + f'Express Software Components: {len(express_software)}\n' \
                     + f'Light Software Components: {len(light_software)}\n' \
                     + f'Memory Usage: {total_used_memory} / {hardware.memory}\n' \
                     + f'Capacity Usage: {total_used_capacity} / {hardware.capacity}\n' \
                     + f'Type: {hardware.hardware_type}\n' \
                     + f"Software Components: {', '.join(total_software) if len(total_software) != 0 else 'None'}"

            result_list.append(result)

        return '\n'.join(result_list)

