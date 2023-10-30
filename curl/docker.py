import numpy as np
import tritonclient.grpc as grpcclient
from tritonclient.utils import *

SERVER_URL = "0.0.0.0:8001"
MODEL_NAME = "{MODEL_NAME}"


def send_request():
    INPUT = (np.random.rand(10) * 100).astype(np.uint8)
    with grpcclient.InferenceServerClient(SERVER_URL) as triton_client:
        inputs = [
            grpcclient.InferInput("INPUT", INPUT.shape, np_to_triton_dtype(np.uint8))
        ]
        inputs[0].set_data_from_numpy(INPUT)
        outputs = [
            grpcclient.InferRequestedOutput("PYTHON"),
        ]

        response = triton_client.infer(
            model_name=MODEL_NAME, inputs=inputs, outputs=outputs
        )

        response.get_response()
        PYTHON = response.as_numpy("PYTHON")
    return PYTHON


if __name__ == "__main__":
    print(send_request())
