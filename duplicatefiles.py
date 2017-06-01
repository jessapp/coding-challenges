# find duplicate files on a file system, and delete the non-original copy

# Strategy: keep a dictionary with the files we've already seen, and their hashed contents and paths
# Compare hash "fingerprints" to see if they're the same file

import os
import hashlib

def find_duplicate_files(directory):

    files_seen = {}

    stack = [directory]

    duplicates = []

    while stack != []:

        current_path = stack.pop()

        # If it's a directory, we add it to the stack

        if os.path.isdir(current_path):
            full_path = os.path.join(current_path, path)
            stack.append(full_path)

        # If it's a file, we hash it and get it's last edited time
        else:

            file_hash = sample_hash_file(current_path)

            current_last_edited_time = os.path.getmtime(current_path)

            # if we've seen it before
            if file_hash in files_seen_already:

                existing_last_edited_time, existing path = files_seen_already[file_hash]

                if current_last_edited_time > existing_last_edited_time:
                    # It is a duplicate

                    duplicates.append((current_path, existing_path))
                else:
                    # the older file is the duplicate
                    duplicates.append((existing_path, current_path))

                    files_seen_already[file_hash] = (current_last_edited_time, current_path)

            else:
                files_seen_already[file_hash] = (current_last_edited_time, current_path)

        return duplicates


def sample_hash_file(path):
    """Function to create hash"""

    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)

    hasher = hashlib.sha512()

    with open(path, 'rb') as file:

        # if the file is too short to take 3 samples, hash the entire file
        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())

        else:
            num_bytes_between_samples = (total_bytes - num_bytes_to_read_per_sample * 3) / 2

            # read first, middle, and last bytes
            for offset_multiplier in xrange(3):
                start_of_sample = offset_multiplier * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    return hasher.hexdigest()
