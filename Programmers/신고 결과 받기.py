def solution(id_list, report, k):
    dic_report = {id: [] for id in id_list}
    answer = [0] * len(id_list)
    for report in set(report):
        report = report.split(' ')
        dic_report[report[1]].append(report[0])
    for key, value in dic_report.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1
    return answer
