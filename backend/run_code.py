import subprocess
import os

def run_code(code, language="python"):
    try:
        if language == "python":
            result = subprocess.run(
                ["python3", "-c", code], capture_output=True, text=True
            )
            return result.stdout if result.returncode == 0 else result.stderr

        elif language == "cpp":
            temp_cpp = "temp.cpp"
            temp_exe = "temp.out"
            
            with open(temp_cpp, "w") as f:
                f.write(code)
            subprocess.run(["g++", temp_cpp, "-o", temp_exe], capture_output=True)

            result = subprocess.run([f"./{temp_exe}"], capture_output=True, text=True)

            os.remove(temp_cpp)
            os.remove(temp_exe)
            
            return result.stdout if result.returncode == 0 else result.stderr

        elif language == "java":
            temp_java = "Main.java"
            temp_class = "Main.class"
            
            with open(temp_java, "w") as f:
                f.write(code)
            subprocess.run(["javac", temp_java], capture_output=True)

            result = subprocess.run(["java", "Main"], capture_output=True, text=True)

            os.remove(temp_java)
            os.remove(temp_class)
            
            return result.stdout if result.returncode == 0 else result.stderr

        else:
            return "Unsupported Language"

    except Exception as e:
        return str(e)