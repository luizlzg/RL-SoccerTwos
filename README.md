# RL-SoccerTwos
Time: Bola Murcha <br>
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

Avaliação feita contra um agente aleatório: <br>
Resumo: <br>
Bola Murcha: Win Rate - 53% <br>
Random: Win Rate - 16% <br>
<pre>
Bola Murcha vs Random  <br>

episode_len_mean: 577.33 <br>
episode_reward_max: 0.0 <br>
episode_reward_mean: -0.534343957901001 <br>
episode_reward_min: -1.9407999515533447 <br>
episodes_this_eval: 100 <br>
policies: <br>
   bola_murcha: <br>
    blue_team: <br>
      policy_blue_team_draws: 14 <br>
      policy_blue_team_losses: 8 <br>
      policy_blue_team_reward_max: 1.9423999786376953 <br>
      policy_blue_team_reward_mean: 0.3731839656829834 <br>
      policy_blue_team_reward_min: -2.0 <br>
      policy_blue_team_total_games: 50 <br>
      policy_blue_team_win_rate: 0.56 <br>
      policy_blue_team_wins: 28 <br>
    orange_team: <br>
      policy_orange_team_draws: 17 <br>
      policy_orange_team_losses: 8 <br>
      policy_orange_team_reward_max: 1.9428000450134277 <br>
      policy_orange_team_reward_mean: 0.3330399692058563 <br>
      policy_orange_team_reward_min: -2.0 <br>
      policy_orange_team_total_games: 50 <br>
      policy_orange_team_win_rate: 0.5 <br>
      policy_orange_team_wins: 25 <br>
    policy_draws: 31 <br>
    policy_losses: 16 <br>
    policy_reward_max: 1.9428000450134277 <br>
    policy_reward_mean: 0.35311198234558105 <br>
    policy_reward_min: -2.0 <br> 
    policy_total_games: 100 <br>
    policy_win_rate: 0.53 <br>
    policy_wins: 53 <br>
  random_agent: <br>
    blue_team: <br>
      policy_blue_team_draws: 17 <br>
      policy_blue_team_losses: 25 <br>
      policy_blue_team_reward_max: 1.9052000045776367 <br>
      policy_blue_team_reward_mean: -0.8077520132064819 <br>
      policy_blue_team_reward_min: -2.0 <br>
      policy_blue_team_total_games: 50 <br>
      policy_blue_team_win_rate: 0.16 <br>
      policy_blue_team_wins: 8 <br>
    orange_team: <br>
      policy_orange_team_draws: 14 <br>
      policy_orange_team_losses: 28 <br>
      policy_orange_team_reward_max: 1.787600040435791 <br>
      policy_orange_team_reward_mean: -0.9671600461006165 <br>
      policy_orange_team_reward_min: -2.0 <br>
      policy_orange_team_total_games: 50 <br>
      policy_orange_team_win_rate: 0.16 <br>
      policy_orange_team_wins: 8 <br>
    policy_draws: 31 <br>
    policy_losses: 53 <br>
    policy_reward_max: 1.9052000045776367 <br>
    policy_reward_mean: -0.8874559998512268 <br>
    policy_reward_min: -2.0 <br>
    policy_total_games: 100 <br>
    policy_win_rate: 0.16 <br>
    policy_wins: 16 <br>

