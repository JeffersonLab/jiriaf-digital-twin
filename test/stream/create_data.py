import json


def combine_json():
    data_files = [
        "/workspaces/UAV-Digital-Twin/test/stream/sim_init_sensor_data/fs_l100_cpu2.json",
        "/workspaces/UAV-Digital-Twin/test/stream/sim_init_sensor_data/fs_l100_cpu8.json",
    ]

    # combine the json files
    output = []
    for file in data_files:
        with open(file, "r") as f:
            data = json.load(f)
            output.extend(data)

    return output



def gen_data(data, num_data):
    # read file as data
    # with open(data_file, "r") as f:
    #     data = json.load(f)
        
    output = {}


    for item in data:
        traffic_intensity = item["TrafficIntensity"]
        parallelism = item["Parallelism"]
        service_rate = item["ServiceRate"]
        len_queue = item["LengthOfQueue"]

        # redefine the parallelism to "2g" if parallelism is 1 and "3g" if parallelism is 2
        if parallelism == 2:
            parallelism = "3g"
        elif parallelism == 8:
            parallelism = "2g"
        else:
            print(f"Parallelism is beyond the range: {parallelism}")
            continue


        # Determine the group based on traffic intensity from 80 to 120 and 5 groups
        group = None
        if 0 <= traffic_intensity < 0.2:
            group = "0"
        elif 0.2 <= traffic_intensity < 0.4:
            group = "20"
        elif 0.4 <= traffic_intensity < 0.6:
            group = "40"
        elif 0.6 <= traffic_intensity < 0.8:
            group = "60"
        elif 0.8 <= traffic_intensity <= 1:
            group = "80"
        else:
            print(f"Traffic intensity is beyond the range: {traffic_intensity}")
            continue

        # Define the another group based on the len_queue from 0 to 5 and 5 groups
        group_2 = None
        if 0 <= len_queue < 1:
            group_2 = "0"
        elif 1 <= len_queue < 2:
            group_2 = "20"
        elif 2 <= len_queue < 3:
            group_2 = "40"
        elif 3 <= len_queue < 4:
            group_2 = "60"
        elif 4 <= len_queue <= 5:
            group_2 = "80"
        else:
            print(f"Length of queue is beyond the range: {len_queue}")
            continue


        
    # output should have the structure like output[group][group_2][parallelism] = [service_rate]
        if group not in output:
            output[group] = {}
        if group_2 not in output[group]:
            output[group][group_2] = {}
        if parallelism not in output[group][group_2]:
            output[group][group_2][parallelism] = {"mean": []}

        output[group][group_2][parallelism]["mean"].append(service_rate)


    # slice the first 100 data
    for key in output:
        for key_2 in output[key]:
            for key_3 in output[key][key_2]:
                output[key][key_2][key_3]["mean"] = output[key][key_2][key_3]["mean"][:num_data]
                if len(output[key][key_2][key_3]["mean"]) != num_data:
                    print(f"Data is not enough for {key} {key_2} {key_3}, len: {len(output[key][key_2][key_3]['mean'])}")
                    continue
                    
    # write to file
    with open("dt_input_config.json", "w") as f:
        json.dump(output, f, indent=4)




def calculate_distribution(date_file):

    # Load the data
    with open(date_file) as f:
        data = json.load(f)

    # Initialize the groups
    groups = {str(i): {"traffic_intensity": 0, "LengthOfQueue": 0} for i in range(0, 100, 20)}

    # Calculate the distribution of traffic_intensity
    for item in data:
        traffic_intensity = item["TrafficIntensity"]
        if 0 <= traffic_intensity < 0.2:
            groups["0"]["traffic_intensity"] += 1
        elif 0.2 <= traffic_intensity < 0.4:
            groups["20"]["traffic_intensity"] += 1
        elif 0.4 <= traffic_intensity < 0.6:
            groups["40"]["traffic_intensity"] += 1
        elif 0.6 <= traffic_intensity < 0.8:
            groups["60"]["traffic_intensity"] += 1
        elif 0.8 <= traffic_intensity <= 1:
            groups["80"]["traffic_intensity"] += 1
        else:
            print(f"Traffic intensity is beyond the range: {traffic_intensity}")

    # Calculate the distribution of LengthOfQueue
    for item in data:
        LengthOfQueue = item["LengthOfQueue"]
        if 0 <= LengthOfQueue < 0.1:
            groups["0"]["LengthOfQueue"] += 1
        elif 0.1 <= LengthOfQueue < 0.2:
            groups["20"]["LengthOfQueue"] += 1
        elif 0.2 <= LengthOfQueue < 0.3:
            groups["40"]["LengthOfQueue"] += 1
        elif 0.3 <= LengthOfQueue < 0.4:
            groups["60"]["LengthOfQueue"] += 1
        elif 0.4 <= LengthOfQueue <= 0.5:
            groups["80"]["LengthOfQueue"] += 1
        else:
            print(f"LengthOfQueue is beyond the range: {LengthOfQueue}")

    print(groups)

    return groups

if __name__ == "__main__":
    gen_data(combine_json(), 24)
    # calculate_distribution("/workspaces/UAV-Digital-Twin/test/stream/sim_init_sensor_data/fs_l100_cpu8.json")            