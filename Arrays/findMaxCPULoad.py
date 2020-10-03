from heapq import *


class job:
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load

  def __lt__(self, other):
    # min heap based on job.end
    return self.end < other.end

def find_max_cpu_load(jobs):
  jobs.sort(key=lambda x: x.start)
  start, end, maxload = jobs[0].start, jobs[0].end, jobs[0].cpu_load

  for i in range(1, len(jobs)):
    job = jobs[i]

    if job.start <= end:
      end = max(job.end, end)
      maxload += job.cpu_load
    else:
      start = job.start
      end = job.end
      maxload = max(maxload, job.cpu_load)

  return maxload

def find_max_cpu_load2(jobs):
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0

    minHeap = []

    for job in jobs:
        
        while len(minHeap) > 0 and job.start >= minHeap[0].end:
            current_cpu_load -= minHeap[0].cpu_load
            heappop(minHeap)

        heappush(minHeap, job)
        current_cpu_load += job.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)

    return max_cpu_load

def main():
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))

def main2():
  print("Maximum CPU load at any time: " + str(find_max_cpu_load2([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load2([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load2([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))

main()
main2()
