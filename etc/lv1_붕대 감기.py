def solution(bandage, health, attacks):
    max_health = health  # 최대 체력
    total_time = 0  # 총 누적 시간
    attack_count = 0  # 누적 공격 횟수
    cont_count = 0  # 연속 회복 횟수
    recovery = bandage[1]  # 회복량
    additional_recov = bandage[2]  # 추가 회복; y
    
    for curr in range(1, attacks[-1][0] + 1):
        if (curr == attacks[attack_count][0]):  # 공격받음
            health -= attacks[attack_count][1]
            attack_count += 1
            cont_count = 0
        else:
            health = min(max_health, health + recovery)  # 회복
            cont_count += 1
            
            if (cont_count == bandage[0]):  # 추가 회복
                health = min(max_health, health + bandage[2])
                cont_count = 0
                
        total_time += 1
        
        if health <= 0:
            return -1
    return health
