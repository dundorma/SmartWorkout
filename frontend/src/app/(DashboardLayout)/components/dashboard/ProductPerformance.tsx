import {
    Typography, Box,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
    Chip
} from '@mui/material';
import DashboardCard from '@/app/(DashboardLayout)/components/shared/DashboardCard';

const workouts = [
    {
        id: "1",
        date: "2024-05-01",
        type: "Cardio",
        workout: "Morning Run",
        intensity: "Low",
        ibg: "primary.main",
        duration: "30",
    },
    {
        id: "2",
        date: "2024-05-02",
        type: "Strength",
        workout: "Weight Lifting",
        intensity: "Medium",
        ibg: "secondary.main",
        duration: "45",
    },
    {
        id: "3",
        date: "2024-05-03",
        type: "Yoga",
        workout: "Evening Yoga",
        intensity: "High",
        ibg: "error.main",
        duration: "60",
    },
    {
        id: "4",
        date: "2024-05-04",
        type: "HIIT",
        workout: "HIIT Workout",
        intensity: "Critical",
        ibg: "success.main",
        duration: "20",
    },
    {
        id: "5",
        date: "2024-05-05",
        type: "Flexibility",
        workout: "Stretching Routine",
        intensity: "Low",
        ibg: "primary.main",
        duration: "15",
    },
];

const WorkoutPerformance = () => {
    return (
        <DashboardCard title="Workout Performance">
            <Box sx={{ height: '400px', overflowY: 'auto', width: { xs: '280px', sm: 'auto' } }}>
                <Table
                    aria-label="simple table"
                    sx={{
                        whiteSpace: "nowrap",
                        mt: 2
                    }}
                >
                    <TableHead>
                        <TableRow>
                            <TableCell>
                                <Typography variant="subtitle2" fontWeight={600}>
                                    Id
                                </Typography>
                            </TableCell>
                            <TableCell>
                                <Typography variant="subtitle2" fontWeight={600}>
                                    Date
                                </Typography>
                            </TableCell>
                            <TableCell>
                                <Typography variant="subtitle2" fontWeight={600}>
                                    Workout
                                </Typography>
                            </TableCell>
                            <TableCell>
                                <Typography variant="subtitle2" fontWeight={600}>
                                    Intensity
                                </Typography>
                            </TableCell>
                            <TableCell align="right">
                                <Typography variant="subtitle2" fontWeight={600}>
                                    Duration (mins)
                                </Typography>
                            </TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {workouts.map((workout) => (
                            <TableRow key={workout.id}>
                                <TableCell>
                                    <Typography
                                        sx={{
                                            fontSize: "15px",
                                            fontWeight: "500",
                                        }}
                                    >
                                        {workout.id}
                                    </Typography>
                                </TableCell>
                                <TableCell>
                                    <Box
                                        sx={{
                                            display: "flex",
                                            alignItems: "center",
                                        }}
                                    >
                                        <Box>
                                            <Typography variant="subtitle2" fontWeight={600}>
                                                {workout.date}
                                            </Typography>
                                        </Box>
                                    </Box>
                                </TableCell>
                                <TableCell>
                                    <Typography color="textSecondary" variant="subtitle2" fontWeight={400}>
                                        {workout.workout}
                                    </Typography>
                                </TableCell>
                                <TableCell>
                                    <Chip
                                        sx={{
                                            px: "4px",
                                            backgroundColor: workout.ibg,
                                            color: "#fff",
                                        }}
                                        size="small"
                                        label={workout.intensity}
                                    ></Chip>
                                </TableCell>
                                <TableCell align="right">
                                    <Typography variant="h6">{workout.duration} mins</Typography>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </Box>
        </DashboardCard>
    );
};

export default WorkoutPerformance;
