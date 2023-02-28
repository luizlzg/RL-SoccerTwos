# RL-SoccerTwos
Repositório destinado ao trabalho final da disciplina de Aprendizado por Reforço da UFG. <br>

Integrantes: <br>
Luiz Fernando Vidal <br>
Luiz Guilherme Corrêa <br>
Heloisy Rodrigues <br>
Tiago Martins <br>

# Estrutura

Na pasta ppo_agent se encontra a classe do agente que recebe a política já treinada (no arquivo policy_state.pkl). Essa é a classe que será utilizada na competição. <br>

Na pasta códigos se encontram os notebooks que foram utilizados para treinar os modelos. São 3 notebooks: um deles é o treinamento em que se utiliza uma política para o time, enquanto o outro treina uma política de forma individual para um agente e passa suas atualizações para os outros agentes e o último é a tentativa de utilização do DQN.

# Avaliação

Avaliação feita contra um agente aleatório:
Bola Murcha vs Random 

episode_len_mean: 577.33
episode_reward_max: 0.0
episode_reward_mean: -0.534343957901001
episode_reward_min: -1.9407999515533447
episodes_this_eval: 100
policies:
  bola_murcha:
    blue_team:
      policy_blue_team_draws: 14
      policy_blue_team_losses: 8
      policy_blue_team_reward_max: 1.9423999786376953
      policy_blue_team_reward_mean: 0.3731839656829834
      policy_blue_team_reward_min: -2.0
      policy_blue_team_total_games: 50
      policy_blue_team_win_rate: 0.56
      policy_blue_team_wins: 28
    orange_team:
      policy_orange_team_draws: 17
      policy_orange_team_losses: 8
      policy_orange_team_reward_max: 1.9428000450134277
      policy_orange_team_reward_mean: 0.3330399692058563
      policy_orange_team_reward_min: -2.0
      policy_orange_team_total_games: 50
      policy_orange_team_win_rate: 0.5
      policy_orange_team_wins: 25
    policy_draws: 31
    policy_losses: 16
    policy_reward_max: 1.9428000450134277
    policy_reward_mean: 0.35311198234558105
    policy_reward_min: -2.0
    policy_total_games: 100
    policy_win_rate: 0.53
    policy_wins: 53
  random_agent:
    blue_team:
      policy_blue_team_draws: 17
      policy_blue_team_losses: 25
      policy_blue_team_reward_max: 1.9052000045776367
      policy_blue_team_reward_mean: -0.8077520132064819
      policy_blue_team_reward_min: -2.0
      policy_blue_team_total_games: 50
      policy_blue_team_win_rate: 0.16
      policy_blue_team_wins: 8
    orange_team:
      policy_orange_team_draws: 14
      policy_orange_team_losses: 28
      policy_orange_team_reward_max: 1.787600040435791
      policy_orange_team_reward_mean: -0.9671600461006165
      policy_orange_team_reward_min: -2.0
      policy_orange_team_total_games: 50
      policy_orange_team_win_rate: 0.16
      policy_orange_team_wins: 8
    policy_draws: 31
    policy_losses: 53
    policy_reward_max: 1.9052000045776367
    policy_reward_mean: -0.8874559998512268
    policy_reward_min: -2.0
    policy_total_games: 100
    policy_win_rate: 0.16
    policy_wins: 16

