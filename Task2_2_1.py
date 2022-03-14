"""Правило трёх очков за победу (англ. Three points for a win rule) — правило начисления очков футбольным командам
во внутренних национальных чемпионатах, групповых этапах клубных турниров и соревнований национальных сборных,
заключающееся в следующем: за победу команда получает три очка в турнирной таблице, за ничью получает только одно
очко и в случае проигрыша очков не получает."""


class FootballTeam:
    def __init__(self, won, draw, failed, scored, missed):
        self.games_won = won  # количество выигранных игр
        self.games_draw = draw  # количество ничейных игр
        self.games_failed = failed  # количество проигранных игр
        self.goals_scored = scored  # количество забитых голов
        self.goals_missed = missed  # количество пропущенных голов
        self.name = "{Name is undefined}"

    # добавить результат матча в формате - {количество забитых голов}, {количество пропущенных голов}.
    def get_match_result(self):
        print("Команда {}. Количество забитых и пропущенных голов соответственно:\n{{{}}}, {{{}}}"
              .format(self.name,
                      self.goals_scored,
                      self.goals_missed))

    # подсчет количества очков заработанных клубом (победа - 3, ничья - 1)
    def count_club_points(self):
        general_points = self.games_won * 3 + self.games_draw
        arg = self.get_subtraction()
        if arg == "win":
            general_points_upd = general_points + 3
        elif arg == "draw":
            general_points_upd = general_points + 1
        else:
            general_points_upd = general_points
        print(
            "Количество очков заработанных клубом: {}.\nКоличество очков заработанных клубом с учетом последнего результата: {}.".format(
                general_points, general_points_upd))

    # подсчет разницы забитых и пропущенных голов
    def get_subtraction(self):
        substr_abs = abs(self.goals_scored - self.goals_missed)
        res = " "
        if self.goals_scored > self.goals_missed:
            print("Победа! Количество забитых голов больше, чем количество пропущенных на: {}.".format(substr_abs))
            res = "win"
        elif self.goals_scored < self.goals_missed:
            print("Поражение! Количество забитых голов меньше, чем количество пропущенных на: {}.".format(substr_abs))
            res = "fail"
        elif self.goals_scored == self.goals_missed:
            print("Ничья. Количество забитых голов равно количеству пропущенных.")
            res = "draw"
        else:
            pass

        return res


# Расширить класс методом, который подсчитывает общее количество игр для команды.
class FootballTeamGames(FootballTeam):
    def __init__(self, won, draw, failed, scored, missed):
        super().__init__(won, draw, failed, scored, missed)

    def get_games_number(self):
        count = self.games_won + self.games_draw + self.games_failed
        print("Общее количество игр для команды: {}.".format(count))


if __name__ == '__main__':
    team1 = FootballTeam(2, 3, 4, 9, 8)
    team1.name = "A"
    team1.get_match_result()
    team1.count_club_points()
    team2 = FootballTeam(4, 4, 4, 11, 8)
    team2.name = "B"
    team2.get_match_result()
    team2.count_club_points()
    team3 = FootballTeamGames(3, 6, 5, 2, 2)
    team3.name = "C"
    team3.get_match_result()
    team3.get_games_number()
