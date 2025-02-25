import sys
import os
import multiprocessing

def process_chunk(chunk, date, output_file):
    matching_lines = [line for line in chunk if line.startswith(date)]
    if matching_lines:
        with open(output_file, "a", encoding="utf-8") as out_file:
            out_file.writelines(matching_lines)

def extract_logs(file_path, date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{date}.txt")
    
    try:
        chunk_size = 10**7 
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        
        with open(file_path, "r", encoding="utf-8") as log_file:
            chunk = []
            for line in log_file:
                chunk.append(line)
                if len(chunk) >= chunk_size:
                    pool.apply_async(process_chunk, (chunk, date, output_file))
                    chunk = []
            
            if chunk:
                pool.apply_async(process_chunk, (chunk, date, output_file))
        
        pool.close()
        pool.join()
        print(f"Logs for {date} have been extracted to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file_path> YYYY-MM-DD")
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    date = sys.argv[2]
    
    extract_logs(log_file_path, date)
