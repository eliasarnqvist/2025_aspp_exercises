from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

value = rank
total = comm.reduce(value, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Sum of ranks from all {size} processes: {total}")
    expected = sum(range(size))
    print(f"Expected: {expected}")
