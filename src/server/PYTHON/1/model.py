import random
import time

import numpy as np
import triton_python_backend_utils as pb_utils


class TritonPythonModel:
    def initialize(self, pbtxt_args):
        print("PYTHON")

    def execute(self, requests):
        responses = []
        for request in requests:
            input = pb_utils.get_input_tensor_by_name(request, "INPUT")
            print(input.as_numpy())
            PYTHON = random.randrange(0, 10)
            print(PYTHON)
            for i in range(PYTHON + 1):
                print(f"PYTHON: time.sleep({i})")
                time.sleep(1)
            output_0 = pb_utils.Tensor("PYTHON", np.array([PYTHON]).astype(np.float32))
            inference_response = pb_utils.InferenceResponse(output_tensors=[output_0])
            responses.append(inference_response)
        return responses

    def finalize(self):
        print("Cleaning up PYTHON Module...")
