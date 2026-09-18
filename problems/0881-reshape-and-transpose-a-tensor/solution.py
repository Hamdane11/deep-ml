import torch
import numpy as np 

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    # TODO: flatten x to 1-D, then rearrange into new_shape
    
    d = np.prod(new_shape)

    x_flat = x.flatten()
    if x.numel() != d :
        print("We cannot reshape into inappropriate dimension.")
    else:
        return x_flat.reshape(new_shape)




def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
   # TODO: swap the last two dimensions of x
    return x.transpose(-1,-2)


